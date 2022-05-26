# scaraper for the political bias chart

# There's a handy API to call
# API = https://app.adfontesmedia.com/api

import requests, json
from datetime import datetime

def main():
    
    date = datetime.today().strftime('%Y_%m_%d')
    '''Get the latest political bias data from adfont'''
    response = requests.get('https://app.adfontesmedia.com/api')
    with open('Data_Collection_And_Filtering/Scraper/chart_data_'+date+'.json', 'w') as f:
        json.dump(response.json(), f)

if __name__ == '__main__':
    main()
