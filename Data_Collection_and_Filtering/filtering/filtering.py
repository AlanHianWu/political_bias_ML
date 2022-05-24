'''pathing for this might be a bit odd, need fix'''
# from Political_News_Filter.political_news_filter import Classifier
# from political_news_filter import Classifier
from tqdm import tqdm
import csv, glob, os

'''filter out news to only political news'''

def filter(file):
    

    classifier = Classifier()
    output_articles = []
    output_bias = []
    
    current_dir =  os.path.abspath(os.path.dirname(__file__))
    Data_dir = os.path.abspath(current_dir + "/../../Data/")
    list_of_files = glob.glob(Data_dir+'/*.tsv')
    latest_file = max(list_of_files, key=os.path.getctime)

    print(latest_file)

    with open(latest_file, encoding="utf8", errors="ignore") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            output_articles.append(row[0])
            output_bias.append(row[1])

    # with open('Data/political_filtered_articles00.tsv', 'a') as out_file:
    #     tsv_writer = csv.writer(out_file, delimiter="\t")
        
    #     print("starting AI")
    #     probs = classifier.estimate(output_articles)

    #     for p in tqdm(range(len(probs)), desc="writing...."):
    #         if probs[p] >= 0.5:
    #             tsv_writer.writerow([output_articles[p], output_bias[p]])
    #         else:
    #             tsv_writer.writerow([output_articles[p], 0])





if __name__ == "__main__":
    current_dir =  os.path.abspath(os.path.dirname(__file__))
    Data_dir = os.path.abspath(current_dir + "/../../Data/")
    list_of_files = glob.glob(Data_dir+'/*.tsv')
    latest_file = max(list_of_files, key=os.path.getctime)
    # print('DIR -> :',Data_dir+'*.tsv', list_of_files)
    print(latest_file)


    
    # filter("articles_data00.tsv")
    # f = filter_news(news)
    # print(len(f))
    pass