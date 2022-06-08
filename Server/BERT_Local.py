'''BERT'''

'''imports'''
import pandas as pd
import numpy as np 
import tensorflow as tf 
import transformers

class BERT_trainer(object):
    def __init__(self):
        pass

    def regular_encoder(self, text, tokenizer, maxlen=512):
        
        pass
    
    def encode_names(self, n, tokenizer):
       tokens = list(tokenizer.tokenize(n))
       tokens.append('[SEP]')
    
       return tokenizer.convert_tokens_to_ids(tokens)
   
   
    def bert_encode(self, string_list, tokenizer, max_seq_length):
        num_examples = len(string_list)
  
        string_tokens = tf.ragged.constant([self.encode_names(n, tokenizer) for n in np.array(string_list)])

        cls = [tokenizer.convert_tokens_to_ids(['[CLS]'])]*string_tokens.shape[0]
        input_word_ids = tf.concat([cls, string_tokens], axis=-1)

        input_mask = tf.ones_like(input_word_ids).to_tensor(shape=(None, max_seq_length))

        type_cls = tf.zeros_like(cls)
        type_tokens = tf.ones_like(string_tokens)
        input_type_ids = tf.concat(
            [type_cls, type_tokens], axis=-1).to_tensor(shape=(None, max_seq_length))

        inputs = {
            'input_word_ids': input_word_ids.to_tensor(shape=(None, max_seq_length)),
            'input_mask': input_mask,
            'input_type_ids': input_type_ids}

        return inputs
    
    def train(self, ):
        pass
    
    def build_model(self, transformer, loss='categorical_crossentropy', maxlen=512):
        pass
    
    def save():
        pass
    
    def load():
        pass


def main():
    bt = BERT_trainer()
    tokenizerSaved = bert.tokenization.FullTokenizer(vocab_file=os.path.join("../" + model_fname, 'assets/vocab.txt'),do_lower_case=False)
    res = bt.bert_encode('I hate my life what should i do from now on??', tokenizer=tokenizerSaved, max_seq_length=426)
    print(res)
    pass





if __name__ == '__main__':
    main()