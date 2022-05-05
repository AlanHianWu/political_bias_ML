
# install these
# pip install tensorflow_hub
# pip install keras tf-models-official pydot graphviz
# pip install bert-tensorflow - Brendan
# scipy too - Brendan

# imports =====================================
from sklearn.preprocessing import LabelEncoder
import numpy as np
from numpy.testing import rundocs
import official.nlp.bert.bert_models
from official.nlp import bert
#import bert # Brendan
#import bert_tensorflow # Brendan
import matplotlib.pyplot as plt
# import tokenization # Brendan
import os # Brendan
import tensorflow as tf # Brendan
# import bert # Brendan
# from bert import bert_tokenization # Brendan
# =============================================


# functions to make the input string tokens since the machine model only read this format
# i have't got this to work yet since i can't install tf-models-official on windows
# =============================================
def encode_names(n, tokenizer):
   tokens = list(tokenizer.tokenize(n))
   tokens.append('[SEP]')
   return tokenizer.convert_tokens_to_ids(tokens)

def bert_encode(string_list, tokenizer, max_seq_length):
  num_examples = len(string_list)

  string_tokens = tf.ragged.constant([
      encode_names(n, tokenizer) for n in np.array(string_list)])

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
# =============================================

# make sure the file paths for 'news_articles_classes.npy' and "article_BERT_first" is set corretly
if __name__ == "__main__":

    # setting the paths
    encoder_fname = 'news_articles_classes.npy'
    model_fname = "article_BERT_first"

    # loading in the the tokenization
    tokenizerSaved = bert.tokenization.FullTokenizer(vocab_file=os.path.join("./" + model_fname, 'assets/vocab.txt'),do_lower_case=False)
    # tokenizerSaved = tokenization.FullTokenizer(vocab_file=os.path.join("./" + model_fname, 'assets/vocab.txt'),do_lower_case=False)
    encoder = LabelEncoder()
    # loading in the model
    encoder.classes_ = np.load("./" + encoder_fname, allow_pickle=True)
    encoder.classes_

    # test inputs here
    test = ['I hate and love this so much what shout i do??']
    inputs = bert_encode(string_list=list(test), tokenizer=tokenizerSaved, max_seq_length=240)
    prediction = new_model.predict(inputs)
    print(prediction)
    print('article is', 'positive' if encoder.classes_[np.argmax(prediction)]==4 else 'negative')
