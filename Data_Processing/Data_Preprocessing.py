import pandas as pd
import re, nltk


'''Class to preform data preprocessing'''
class Preprocessing(object):

    def __init__(self):
        '''stop words only for english'''
        self.STOPWORDS = set(nltk.stopwords.words('english'))
        pass

    '''Remove special characters'''
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
        return None
    
    '''lemmatization 
        resolving words to their dictionary form
        much better but needs lots more power'''
    
    def lemma_words(self, text):
        return None
    




def main():
    pass


if __name__ == '__main__':
    main()