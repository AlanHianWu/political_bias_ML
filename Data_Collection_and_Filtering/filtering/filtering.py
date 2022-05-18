from political_news_filter import Classifier
from tqdm import tqdm
import csv

'''filter out news to only political news'''

def filter(file):
    classifier = Classifier()
    output_articles = []
    output_bias = []
    with open('large_cleaned_text03.tsv', encoding="utf8", errors="ignore") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            output_articles.append(row[0])
            output_bias.append(row[1])

    with open('political_filtered_articles06.tsv', 'a') as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")
        
        print("starting AI")
        probs = classifier.estimate(output_articles)

        for p in tqdm(range(len(probs)), desc="writing...."):
            if probs[p] >= 0.5:
                tsv_writer.writerow([output_articles[p], output_bias[p]])
            else:
                tsv_writer.writerow([output_articles[p], 0])





if __name__ == "__main__":
    filter("articles_data00.tsv")
    # f = filter_news(news)
    # print(len(f))