# install these
# pip install tensorflow_hub
# pip install keras tf-models-official pydot graphviz

# imports =====================================
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import os
import numpy as np
import official.nlp.bert.tokenization as tokenization
import official.nlp.bert.bert_models
from official.nlp import bert
import matplotlib.pyplot as plt
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
    tokenizerSaved = bert.tokenization.FullTokenizer(vocab_file=os.path.join("../" + model_fname, 'assets/vocab.txt'),do_lower_case=False)
    encoder = LabelEncoder()
    # loading in the model
    encoder.classes_ = np.load("../" + encoder_fname, allow_pickle=True)
    encoder.classes_
    model = tf.keras.models.load_model("../article_BERT_first")

    # test inputs here
    test = ["UK and EU leaders have reiterated their full commitment to the contentious Northern Ireland Protocol following talks in London.A joint statement said that British Cabinet Office minister Michael Gove and European Commission vice president Maros Sefcovic had a frank but constructive discussion this evening, in which they agreed to spare no effort in implementing solutions.The two men agreed to convene a joint committee no later than 24 February to provide the necessary political steer and approval to this work in the spirit of collaboration, responsibility and pragmatism.They said they were intent on protecting the Good Friday Agreement and impacting as little as possible on the everyday life of communities in both Ireland and Northern Ireland.The protocol requires regulatory and customs checks on goods moving from Great Britain to Northern Ireland, but it has caused disruption to trade since it came into force on 1 January, with various grace periods in operation.Unionists are deeply concerned about the arrangements, insisting they have driven an economic wedge between Northern Ireland and the rest of the UK. They have called on the UK to trigger a mechanism within the protocol - Article 16 - which enables the government to unilaterally suspend aspects it deems are causing economic, societal or environmental problems. Going into the talks, Mr Sefcovic stressed that implementing the protocol is a two-way street and the UK had to abide by commitments it made in December. Going into the talks, Mr Sefcovic stressed that implementing the protocol is a two-way street and the UK had to abide by commitments it made in December. These must be urgently implemented, he said, after sending a letter to Mr Gove complaining that London was failing to hold up its side of the agreement on matters such as customs checks for goods entering Northern Ireland. We are ready to look into these teething challenges while respecting the objectives of the protocol. We see the protocol as a solution, not a problem, Mr Sefcovic added. Mr Gove had urged Mr Sefcovic to set out rapid action to fix the issues, covering everything from chilled meat rules to pet travel regulations, along with a demand to extend a three-month grace period for supermarkets until 2023. He told MPs ahead of the meeting that the UK was seeking to ensure light touch border processes for trade with Northern Ireland. Read more: Need to dial down rhetoric over protocol, says Martin Latest Brexit stories Fears of sectarian tensions in Northern Ireland were fuelled after the European Commission said it would restrict Covid-19 vaccine exports as the bloc struggles with its own supply. Although the EU quickly backtracked, the move has intensified opposition to the new regulations, and threats against officials forced the temporary suspension of customs checks at Belfast and Larne ports earlier this month.The joint statement papered over the testy exchanges that preceded todays meeting, but agreed that the commitments made by both sides in December form a foundation for our cooperation.Mr Gove and Mr Sefcovic pledged to convene their joint UK-EU committee on Northern Ireland no later than 24 February to provide the necessary political steer and approval to this work in the spirit of collaboration, responsibility and pragmatism."]
    test1 = [test[0][426*2:426*3]]
    inputs = bert_encode(string_list=list(test1), tokenizer=tokenizerSaved, max_seq_length=426)
    prediction = model.predict(inputs)
    print(encoder.classes_[np.argmax(prediction)])