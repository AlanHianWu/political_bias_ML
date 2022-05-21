from matplotlib.font_manager import json_load
from newspaper import Article
import json, newspaper, copy, concurrent.futures, csv
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from sympy import EX
from torch import chunk
from tqdm import tqdm
from itertools import islice
from datetime import datetime


'''class that uses the newpaper3k to get the latest news articles from the json file in scaper'''
class get_news():
    def __init__(self, workers=100):
        self.data = {}
        self.working_urls = []
        self.workers = workers
    
    def get_all_news(self):
        executor = ThreadPoolExecutor(self.workers)

        with ThreadPoolExecutor(max_workers=self.workers) as executor:

            for chunk in self.chunks(self.data, 10):
                executor.submit(self.get_single_news, (chunk))

        self.download_all_articles()
    
    def download_all_articles(self):
        print('\nSTART\n')

        for url in self.working_urls:
            self.download_articles(url)


    def download_articles(self, url):
        try:
            article = Article(url[0])
            article.download()
            article.parse()
        
            article.text = " ".join(article.text.split())
            data = [article.text, url[1]]    
            date = datetime.today().strftime('%Y-%m-%d')

            with open('Data/articles_data_'+date+'_.tsv', 'a', newline='') as f_output:
                tsv_output = csv.writer(f_output, delimiter='\t')
                tsv_output.writerow(data)

        except Exception as e:
            print('fail write', e)
        

    def get_single_news(self, chunk):
        
        '''needs to be threaded'''
        for domain in tqdm(chunk.keys(), desc="building webpages....."):
        # for domain in chunk.keys():
            try:
                
                paper = newspaper.build(chunk[domain]['main_url'])
                
                for article in paper.articles:
                    self.working_urls.append((article.url, chunk[domain]['bias']))
            except Exception as e:
                print('fail to build paper', e)
                pass

    
    def get_latest_data(self):
        
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
        "reach": 4100, 
        "mediatype": 2, 
        "article_count": 3, 
        "bias": 0.0, 
        "reliability": 43.33333, 
        "all_metrics": {"15": 0.0, "16": 0.0, "17": 0.0, "22": 0.0, "26": 43.0, "27": 43.0, "28": 44.0, "32": 43.33333, "34": 43.0}}'''
        '''gets the latest Data from https://app.adfontesmedia.com/api'''
        
        #update self.data with json file

        data = json_load('Data_Collection_And_Filtering/Scraper/chart_data.json')
        for i in data:
            self.data[i['domain']] = {'main_url': i['main_url'],
                                      'url': i['url'], 
                                      'bias': i['bias'], 
                                      'score_count': i['score_count'], 
                                      'reach': i['reach'], 
                                      'article_count': i['article_count'], 
                                      'reliability': i['reliability']}

        '''update self.data'''
        # print(len(self.data))

    '''split data into chunks for thrends'''

    def chunks(self, data, SIZE=1):
        lenght = len(data)

        if SIZE <= lenght and SIZE >= 1:
            it = iter(data)
            for i in range(0, lenght, SIZE):
                yield {k:data[k] for k in islice(it, SIZE)}
        else:
            return False



def main():
    gn = get_news()
    
    gn.get_latest_data()
    # gn.get_single_news()
    gn.get_all_news()
    
    # gn.download_all_articles()
    
    # data = {1:1, 2:2, 3:3, 4:4, 5:5}
    # for n in  gn.chunks(data, 5):
    #   print(n)  
    
    
    # cnn_paper = newspaper.build('http://cnn.com')

    # for article in cnn_paper.articles:
    #     print(article.url)





if __name__ == '__main__':

    main()


