#https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
#import pandas as pd
#from sklearn import preprocessing

# Used for asynchronous functions
import asyncio
# Used to fake user-agent in outbound HTTP(s) requests
from fake_useragent import UserAgent
# Used to parse HTML files and find elements
from bs4 import BeautifulSoup
# Used to make HTTP(s) requests
import requests
from requests_html import HTMLSession
#from requests_html import AsyncHTMLSession


# Retrieve the instances of elements that match ID: #sourceAverage
def get_data():
    session = HTMLSession()
    #asession = AsyncHTMLSession()
    #r = await asession.get('https://public-interactive-chart.vercel.app/')
    #  Retrive the content from the internet
    r = session.get('https://public-interactive-chart.vercel.app/')
    # Run a javascript engine to render the HTML properly
    r.html.render()
    #print(r.html.html)
    #bias = r.html.find('sourceAverage', first=True)
    bias = r.html.find('#sourceAverage', first=True)
    print(bias)

# Similar to get_data function, except from a source file rather than results from a HTTP(s) request
def scrape_from_file():
    with open('output.html', 'r') as f:
        contents = f.read()
        # Initialize bs4
        soup = BeautifulSoup(contents, 'lxml')
        #print(soup.title.text)
        # Find all elements with class of 'sourceAverage'
        bias_list = soup.find_all(class_="sourceAverage")
        bias_dict = {}
        for bias in bias_list:
            #print("BIAS:", bias['x'], "NAME:", bias['href'].split('/')[-1].split('.png')[0])
            bias_value = float(bias['x'])
            #if bias_value < 0:
            #    bias_value = bias_value+804.88
            #else:
                #bias_value = bias_value-432.43
            #    bias_value = bias_value-627.18
            bias_dict[bias['href'].split('/')[-1].split('.png')[0]] = bias_value
        sort_bias_dict = sorted(bias_dict.items(), key=lambda x: x[1], reverse=True)

        for i in sort_bias_dict:
            print(i[0], i[1])
        #for i in sorted (bias_dict.keys()):
        #    print(i, bias_dict[i])
        #for bias in bias_dict:
        #    print(bias, bias_dict[bias])

if __name__ == "__main__":
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
