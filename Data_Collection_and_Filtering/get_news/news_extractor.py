from matplotlib.font_manager import json_load
from newspaper import Article
import json, newspaper
from concurrent.futures import ThreadPoolExecutor
from time import sleep

class get_news():
    def __init__(self):
        pass
    
    def get_all_news(self):
        pass
    
    def get_single_news(self, url):
        
        paper = newspaper.build(url)

        for article in paper.articles:
            #article url
            pass
        
        for category in paper.category_urls():
            pass
            



def task(message):
    sleep(2)
    return message
    
def test():
    executor = ThreadPoolExecutor(5)
    future = executor.submit(task, ('completed'))
    print(future.done())
    sleep(2)
    print(future.done())
    print(future.result())


def main():
    '''Be a bit careful here with handling the data, there is a lot of details, like this goes into specific articles etc'''
    '''example segment:
        {"article_id": 18194, 
        "source_id": 1169, 
        "url": "https://www.readtangle.com/p/united-states-biden-strike-syria", 
        "score_count": 3, 
        "domain": ".readtangle.com", 
        "main_url": "https://www.readtangle.com", 
        "moniker_name": "Tangle", 
        "image_path": "www_readtangle_com.png", 
        "reach": 4100, "mediatype": 2, 
        "article_count": 3, 
        "bias": 0.0, 
        "reliability": 43.33333, 
        "all_metrics": {"15": 0.0, "16": 0.0, "17": 0.0, "22": 0.0, "26": 43.0, "27": 43.0, "28": 44.0, "32": 43.33333, "34": 43.0}}'''

    data = json_load('Data_Collection_And_Filtering/Scraper/chart_data.json')
    for i in data:
        print(i['moniker_name'], i['url'], i["bias"])

    newspaper.build()


if __name__ == '__main__':
    test()
    # main()


