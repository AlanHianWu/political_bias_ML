# scaraper for the political bias chart

# There's a handy API to call 
# API = https://app.adfontesmedia.com/api

import requests

def main():
    '''Get the latest political bias data from adfont'''
    response = requests.get('https://app.adfontesmedia.com/api')
    print(response.json())


if __name__ == '__main__':
    main()
