import newspaper
from newspaper import Article
import csv

all_papers = []


with open("./data/adfontesmedia.csv", "r") as news_websites:
    news = csv.reader(news_websites)
    next(news)
    for line in news:
        all_papers.append((line[1], line[2]))

working_urls = []

for paper in all_papers[15:17]:
    print("building", paper)
    news_paper = newspaper.build(paper[0])
    for article in news_paper.articles:
        print(article.url)
        working_urls.append((article.url, paper[1]))

print(working_urls)

for url in working_urls:
    try:
        article = Article(url[0])
        article.download()
        article.parse()
    
        data = [article.text, url[1]]    

        with open('articles_data.tsv', 'a', newline='') as f_output:
            tsv_output = csv.writer(f_output, delimiter='\t')
            tsv_output.writerow(data)
    
    
        # with open("./articles/" + article.title + "txt", "w") as new_article:
        #     new_article.write(article.text)
    except:
        print("not working")


