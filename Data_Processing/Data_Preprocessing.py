import pandas as pd
import re, os, glob

'''for concurrent'''
from concurrent.futures import ThreadPoolExecutor

'''might need processes'''
from multiprocessing import Process

'''stop words'''
from nltk.corpus import stopwords
# nltk.download('stopwords') '''might need to download or update stopwords'''

'''steming'''
from nltk.stem import PorterStemmer

'''lemmatization'''
from nltk.stem import WordNetLemmatizer

'''Class to preform data preprocessing'''
class Preprocessing(object):

    def __init__(self, workers=2):
        #stop words only for english
        self.STOPWORDS = set(stopwords.words('english'))
        
        '''for now used to define concurrent workers count'''
        self.workers = workers

    #Remove special characters
    def remove_special_characters(self, text, remove_digits=True):
        pattern = r'[^a-zA-Z0-9\s]' if not remove_digits else r'[^a-zA-Z\s]'
        text = re.sub(pattern, '', text)
        return text

    '''useless words are know as stopwords this function is here to get rid of stop words,
       this is done by using nltk built in Stop words'''
    def remove_stopwords(self, text):
        """custom function to remove the stopwords"""
        return " ".join([word for word in str(text).split() if word not in self.STOPWORDS])
    
    '''steming
       reducing a word to it's stem, meaning eg words ending in "ed", "ing" ect.. gets reduced'''
    '''cons:
        * it can suffer from over stemming or under stemming'''
    def stem_words(self, text):
        stemmer = PorterStemmer()
        return stemmer.stem(text)
    
    '''lemmatization 
        resolving words to their dictionary form
        much better but needs lots more power'''
    
    def lemma_words(self, text):
        lemmatizer = WordNetLemmatizer()
        return lemmatizer.lemmatize(text)
    
    '''case convert, convert all case of words to lower'''
    def lower_case(self, text):
        return text.lower()
    
    '''remove white space/ emtpy data'''
    def remove_emtpy(self, text):
        pass
    
    '''interesting one to do, needs to hard remove duplicates in the entire dataset'''
    def remove_dups(self, text):
        pass
    
    '''always a big headache, need to truncate the data so it fits the ram size and 
       retains the info'''
    def truncate(self, text, length):
        pass


def main():
    pass
    # pp = Preprocessing()
    # stemmed = pp.stem_words('')
    # print(stemmed)
    current_dir =  os.path.abspath(os.path.dirname(__file__))
    json_dir = os.path.abspath(current_dir + "/../Data")
    list_of_files = glob.glob(json_dir + '/*.tsv')
    latest_file = max(list_of_files, key=os.path.getctime)

    '''data not clean yet'''    
    df = pd.read_csv(latest_file, sep='\t', encoding='latin-1')
    
    print(df.head())

if __name__ == '__main__':
    main()