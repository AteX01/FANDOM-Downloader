import requests

def query(url, article):
    files = []
    query_url = f'{url}/api.php?action=query&prop=images&format=json&titles={article}'

    try:
        while True:
            r = requests.get(query_url)
            data = r.json()

            for pageid in data['query']['pages']:
                for file_data in data['query']['pages'][pageid]['images']:
                    files.append(file_data['title'])

            try:
                imcontinue = data['continue']['imcontinue']
                query_url = f'{query_url}&imcontinue={imcontinue}'
            except KeyError:
                break
    except Exception as e:
        print(f'FANDOM API (query) Error: {e}')

    return files

def get_file_url(url, file):
    file = requests.utils.quote(file)
    file_url = f'{url}/api.php?action=query&prop=imageinfo&format=json&iiprop=url&titles={file}'

    try:
        r = requests.get(file_url)
        data = r.json()
        
        for page_id in data['query']['pages']:
            for file_data in data['query']['pages'][page_id]['imageinfo']:
                file_direct_url = file_data['url']
                return file_direct_url
    except Exception as e:
        print(f'FANDOM API (get_file_url) Error: {e}')

    return None
