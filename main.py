import sys, getopt
from src import downloader

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h",['url='])
    except getopt.GetoptError as err:
        try_help()
        return

    for opt, arg in opts:
        if opt == '-h':
            print('Arguments:\n',
                '-h show help\n',
                '--url <url to fandom website>'
            )
            return
        elif opt in ('--url'):
            url = arg

            if url:
                downloader.initialize_download(url)
            return

    try_help()

def try_help():
    print('It\'s not gonna work, arguments are invalid. Try -h for help.')

if __name__ == "__main__":
    main(sys.argv[1:])