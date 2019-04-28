import requests
import os
from src import fandom

def initialize_download(link):
    article_index = link.index('/wiki/')
    
    url = link[:article_index]
    title = url[link.index('://') + 3:link.index('.fandom.com')]
    article = link[article_index+6:]

    download_dir = create_dir(title, article)
    download_files(download_dir, url, article)

def create_dir(title, article):
    article = requests.utils.unquote(article)

    if not os.path.exists(f'DownloadedFiles/{title}/{article}'):
        os.makedirs(f'DownloadedFiles/{title}/{article}')

    return f'DownloadedFiles/{title}/{article}'

def download_files(download_dir, url, article):
    files = fandom.query(url, article)
    files_len = len(files)
    file_count = 1

    for file in files:
        file_direct_url = fandom.get_file_url(url, file)

        if file_direct_url != None:
            file_name = file[file.index('File:')+5:]
            print(f'File {file_count}/{files_len}: Downloading {file_name} from {file_direct_url}')
            r = requests.get(file_direct_url)
            open(f'{download_dir}/{file_name}', 'wb').write(r.content)

        file_count += 1