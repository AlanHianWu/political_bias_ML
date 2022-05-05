#https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
# For interacting with CSV Files
import csv
# For using time delay
import time
# RegEx
import re
# For intneracting with JSON filetype
import json
#import pandas as pd
#from sklearn import preprocessing
#import asyncio
#from fake_useragent import UserAgent
# BS4 used for parsing HTML pages
from bs4 import BeautifulSoup
# Requests used for making HTTP requests
import requests
from requests_html import HTMLSession
#from requests_html import AsyncHTMLSession


# Find HTML elements with ID 'sourceAverage'
def get_data():
    #session = HTMLSession()
    #asession = AsyncHTMLSession()
    #r = await asession.get('https://public-interactive-chart.vercel.app/')
    #r = session.get('https://public-interactive-chart.vercel.app/')
    #r = session.get('https://public-interactive-chart.vercel.app/static/js/main.69379c3a.chunk.js')
    #r.html.render()
    #print(r.html.html)
    #bias = r.html.find('sourceAverage', first=True)
    bias = r.html.find('#sourceAverage', first=True)
    print(bias)

def scrape_sources():
    session = HTMLSession()
    #r = requests.get('https://public-interactive-chart.vercel.app/static/js/main.69379c3a.chunk.js')
    r = session.get('https://public-interactive-chart.vercel.app/static/js/main.69379c3a.chunk.js')
    r.html.render()
    bias_list=r.html.html
    #bias_list = r.text
    #print(bias_list)
    _out = [''] * 9999
    output = ['' for i in re.finditer('url:', bias_list)]
    bias_url = [i.start() for i in re.finditer('url:', bias_list)]
    for j,i in enumerate(bias_url):
        #print(bias_list[i:i+bias_list[i:].index(',')])
        _text = bias_list[i:i+bias_list[i:].index(',')]
        _out[j] += _text.split('//')[1].split('.com')[0].split('.org')[0]
        _out[j] += '\t'
    bias_val = [i.start() for i in re.finditer('bias:', bias_list)]
    for j,i in enumerate(bias_val):
        #print(bias_list[i:i+bias_list[i:].index(',')])
        _text = bias_list[i:i+bias_list[i:].index(',')]
        _out[j] += _text.split('bias:')[1]

    with open("output.csv", "wb") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                quotechar="|", quoting = csv.QUOTE_MINIMAL)
        for i in _out:
            if i != "":
                #print(i)
                filewriter.writerow([i])
        print("output.csv written")

    #    output[i]+= (bias_list[i:i+bias_list[i:].index(',')])
    #bias_val = [i.start() for i in re.finditer('bias:', bias_list)]
    #for i in bias_val:
    #    output[i]+= (bias_list[i:i+bias_list[i:].index(',')])

    #for item in output:
    #    print(item)


    #bias_json = json.loads(bias_list)
    #bias_json = bias_list.split('\n')
    #print(bias_list)
    #for bias in bias_json:
    #    bias_item = json.loads(bias)
    #    print(bias_item)
    #bias_list = r.json()
    #for bias in bias_list:
    #    print(bias)

# Scrape sources from local file
def scrape_from_file():
    with open('output2.html', 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        #print(soup.title.text)
        bias_list = soup.find_all(class_="sourceAverage")
        bias_dict = {}
        urls = get_urls()
        with open("output.csv", "w") as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow(['website', 'url', 'bias', 'reliability'])
            for bias in bias_list:
                #print("BIAS:", bias['x'], "NAME:", bias['href'].split('/')[-1].split('.png')[0])
                bias_value = float(bias['x'])/887.859
                reliability_value = float(bias['y'])/572.81577
                #if bias_value < 0:
                #    bias_value = bias_value+804.88
                #else:
                    #bias_value = bias_value-432.43
                #    bias_value = bias_value-627.18
                bias_name = bias['href'].split('/')[-1].split('.png')[0]
                set_url = ''
                for url in urls:
                    if bias_name.replace('_','') in url:
                        set_url = url

                filewriter.writerow([bias_name, set_url, bias_value, reliability_value])
        print("output.csv written")
                #bias_dict[bias['href'].split('/')[-1].split('.png')[0]] = bias_value
        #sort_bias_dict = sorted(bias_dict.items(), key=lambda x: x[1], reverse=True)

        #with open("output.csv", "w") as csvfile:
        #    #filewriter = csv.writer(csvfile, delimiter=',',
        #    #        quotechar="|", quoting = csv.QUOTE_MINIMAL)
        #    filewriter = csv.writer(csvfile)
        #    filewriter.writerow(['website', 'url', 'bias', 'reliability'])
        #    for i in sort_bias_dict:
        #        print(i[0], i[1])
        #        filewriter.writerow([i[0], i[1]])
        #    print("output.csv written")
        #for i in sorted (bias_dict.keys()):
        #    print(i, bias_dict[i])
        #for bias in bias_dict:
        #    print(bias, bias_dict[bias])

# Extract URLs from the graph instance
def get_urls():
    r = requests.get('https://public-interactive-chart.vercel.app/static/js/main.7f302d46.chunk.js')
    data = r.text
    url_val = [i.start() for i in re.finditer('url:', data)]
    output = []
    for item in url_val:
        _out = (''.join(data[item:item+data[item:].index(',')].split('url:')[1].split('/')[0:3]))
        if _out not in output:
            output.append(_out)
    return list(set(output))




# Save the HTML file locally
def make_output():
    session = HTMLSession()
    r = session.get('https://public-interactive-chart.vercel.app/static/js/main.69379c3a.chunk.js')
    r.html.render()
    #r = requests.get('https://public-interactive-chart.vercel.app/static/js/main.69379c3a.chunk.js')
    _f = open("output2.html", "w")
    #print(r.text)
    #print(r.html.html)
    #_f.write(r.text)
    _f.write(r.html.html)
    _f.close()


if __name__ == "__main__":
    make_output()
    #get_urls()
    time.sleep(3)
    #scrape_sources()
    scrape_from_file()
    #get_data()
    #session = HTMLSession()
    #ua = UserAgent()
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    #headers = {'User-Agent': ua.chrome}
    #page = requests.get('https://www.adfontesmedia.com/interactive-media-bias-chart-2/', headers=headers)
    #page = requests.get('https://public-interactive-chart.vercel.app/', headers=headers)
    #r = session.get('https://public-interactive-chart.vercel.app/')
    #print(r.html.find('#sourceAverage', first=True))
    #soup = BeautifulSoup(r.html.html, "lxml")
    #bias_list = soup.find_all("image")
    #bias_list = soup.find_all("image")
    #print(bias_list)
    #print(r.html.html)
    #print(page.content)

'''
soup = BeautifulSoup(page.content, 'html.parser')
page_title = soup.title.text
page_body = soup.body
page_head = soup.head

#first_bias = soup.find_all("image", class_=["sourceAverage"])
#first_bias = soup.select("image.sourceAverage")
print(page_body)
for link in soup.findAll("image", {'class': 'sourceAverage'}):
    print(link)
'''
