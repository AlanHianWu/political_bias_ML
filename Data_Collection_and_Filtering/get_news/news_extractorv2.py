# better handling for urls, added loading bars to see progress
import newspaper
from newspaper import Article
import csv
from tqdm import tqdm

all_papers = []

with open("./data/new_data_source03.csv", "r") as news_websites:
    news = csv.reader(news_websites)
    next(news)
    for line in news:
        all_papers.append((line[1], line[2]))

working_urls = []

for paper in tqdm(all_papers, desc="building webpages....."):
    try:
        news_paper = newspaper.build(paper[0])
        for article in news_paper.articles:
            working_urls.append((article.url, paper[1]))
    except:
        print(" not working", paper)


print("about ", len(working_urls), "working websites")
for url in tqdm(working_urls, desc="Downloading..."):
    try:
        article = Article(url[0])
        article.download()
        article.parse()
    
        article.text = " ".join(article.text.split())
        data = [article.text, url[1]]    

        with open('articles_data08.tsv', 'a', newline='') as f_output:
            tsv_output = csv.writer(f_output, delimiter='\t')
            tsv_output.writerow(data)
    
    
        # with open("./articles/" + article.title + "txt", "w") as new_article:
        #     new_article.write(article.text)
    except:
        pass
        # print("not working")


