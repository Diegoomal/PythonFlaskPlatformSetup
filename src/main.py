import os

# os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

if __name__ == "__main__":
    
    print(tf.reduce_sum(tf.random.normal([1000, 1000])))
    
    print('\n__main__\n')
