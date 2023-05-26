import os
import random
import numpy as np
import tensorflow as tf


def read_data_files(root, folder, sub_folder, file_name):
    with open(os.path.join(root, folder, sub_folder, file_name)) as f:
        files_names = [line.replace('\n','') for line in f.readlines()]
    return files_names

def read_files_names(root, folder):
    return os.listdir(os.path.join(root, folder))

def read_image(root, folder, file_name) -> None:
    return tf.keras.utils.load_img(
        os.path.join(root, folder, file_name),
        grayscale=False,
        color_mode='rgb',
        target_size=None,
        interpolation='nearest'
    )

def reset_seeds():
    random.seed(123)
    np.random.seed(123)
    tf.random.set_seed(1234)
