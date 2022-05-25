'''Political filter using BERT for classifier'''

'''imports'''
import pandas as pd
import numpy as np 
import tensorflow as tf 
import transformers

class BERT_trainer(object):
    def __init__(self, device=None):
        # Detect Hardware for config
        if device == None:
            # if not specified on the device type look for one
            '''try for tpu'''
            try:
                tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
                print('running on TPU', tpu.master())
            
            except ValueError:
              
                print('No TPU found')
            
            '''try for gpu'''
            try:
                gpu = tf.test.gpu_device_name()
                print('running on GPU', gpu)
            
            except ValueError:
               
                print('No GPU found')
            
            '''try for cpu'''
            try:
                cpu = None
    
                print('running on cpu', cpu)
            
            except ValueError:
                
                print('No CPU found')
            
            
            

    def regular_encoder(self, text, tokenizer, maxlen=512):
        pass
    
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







if __name__ == '__main__':
    main()