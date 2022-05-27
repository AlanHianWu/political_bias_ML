import pandas as pd
import re, os, glob

'''for concurrent'''
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

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

    def __init__(self, file=None, workers=2):
        
        if file == None:
            self.file = self.get_latest_data_file()
        else:
            try:
                with open(file) as f:
                    self.file = pd.read_csv(f, sep='\t', encoding='latin-1')
            except Exception as e:
                print('file does not found', e)

        
        #stop words only for english
        self.STOPWORDS = set(stopwords.words('english'))
        
        '''for now used to define concurrent workers count'''
        self.workers = workers

    # Remove special characters
    def remove_special_characters(self, text, remove_digits=True):
        # pattern = r'[^a-zA-Z0-9\s]' if not remove_digits else r'[^a-zA-Z\s]'
        # text = re.sub(pattern, '', text)
        if not remove_digits:
                pattern = r'[^a-zA-Z0-9\s]' 
        else:
            pattern = r'[^a-zA-Z\s]'

        text = re.sub(pattern, '', text)
        print('yo', current_thread())
        return text
    
    # Remove special characters with threading
    def remove_special_characters_multi(self, text, remove_digits=True):
        

        with ThreadPoolExecutor(max_workers=10) as executor:
            re = []
            for t in self.remove_special_split(text, 100):
                re.append(executor.submit(self.remove_special_characters, (t)))
                '''they will finish at different times order matters ! '''
                # re.append(future.result())
        return re
                


    '''split input to workers for remove special characters'''
    @staticmethod
    def remove_special_split(text, split):
        '''split works with given split length will return the split in that length eg. '[a,a,a,a,a,a]' split=2 will return
                                                                                         [a, a]
                                                                                         [a, a]
                                                                                         [a, a]
        '''
        text = text.split()
        for i in range(0, len(text), split):
            yield " ".join(text[i:i+split])


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
    
    '''remove white space / emtpy data'''
    def remove_emtpy(self, text):
        pass
    
    '''interesting one to do, needs to hard remove duplicates in the entire dataset'''
    def remove_dups(self, text):
        pass
    
    '''always a big headache, need to truncate the data so it fits the ram size and 
       retains the info'''
    def truncate(self, text, length):
        '''idea smart truncate refrase the sentence to somethig shorter??'''
        pass
    
    '''idea here is to remove stuff that does not make sense'''
    def grammer_check():
        pass
    
    '''language check'''
    '''should only foucus on English'''
    def language_check(self, text):
        pass
    
    '''should use to clean up text'''
    def clean_text(self, text):
        pass
    
    '''used to split text bias to certain categories'''
    def split(self, text):
        pass
    
    '''test to see what changes where made'''
    def document_similarity_test(self):
        return None
    
    
    '''use relative pathing to find the latest data file'''
    @staticmethod
    def get_latest_data_file():
        current_dir =  os.path.abspath(os.path.dirname(__file__))
        dir_path = os.path.abspath(current_dir + "/../../Data")
        list_of_files = glob.glob(dir_path + '/*.tsv')
        latest_file = max(list_of_files, key=os.path.getctime)

        '''data not clean yet'''    
        df = pd.read_csv(latest_file, sep='\t', encoding='latin-1')

        # print(df.head())
        
        return df
    '''return self.file'''
    def file(self):
        return self.file

def main():
    pass
    pp = Preprocessing(file=None, workers=10)
    # stemmed = pp.stem_words('')
    # print(stemmed)
    # pp.get_latest_data_file()
    # re = pp.remove_special_characters_multi('haha!@#$%')
    # print(re)
    
    t = '''testingone test**ingtwo te^stingthree testingfour testfive @@ingsix testin!gseven testi@ngeight''' * 1000
    r = pp.remove_special_characters_multi(t)
    for f in r:
        print(f.result())


if __name__ == '__main__':
    main()