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
            self.device = self.find_device()
        else:
            self.device = device
    
    
    '''find and set the device for training'''
    @staticmethod
    def find_device():
        
        '''import tensorflow as tf    

            model = tf.keras.Model(...)

            # Run training on GPU
            with tf.device('/gpu:0'):
                model.fit(...)

            # Run inference on CPU
            with tf.device('/cpu:0'):
                model.predict(...)'''

        '''try for tpu'''
        try:
            tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
            print('running on TPU', tpu.master())
            return 'TPU'
        
        except ValueError:
            print('No TPU found')
        
            '''try for gpu'''
            try:
                gpu = tf.test.gpu_device_name()
                print('running on GPU', gpu)
                return 'GPU'
            
            except ValueError:
                
                print('No GPU found')
            
                '''try for cpu'''
                try:
                    cpu = None
                    print('running on cpu', cpu)
                    return 'CPU'
                
                except ValueError:
                    print('No CPU found')
                    print('No device set')
                    return None


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