import os
import json
import numpy as np

from util import read_files_names
from configs import WIDTH, HEIGHT, CHANNELS, SIZE
from data_augmentation import execute_data_augmentation_operation_on_image_by_path

import tensorflow as tf
tf.config.run_functions_eagerly(True)
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import (Activation, Dropout, Dense, Flatten, 
                                     BatchNormalization, Conv2D, MaxPooling2D,
                                     Input, AveragePooling2D)

def get_all_files_in_path_filtered_by_extesion(
        path_dataset:str = "./src/ebeer_dataset/",
        filter_file_ext: list[str] = [".jpg", ".png", "json"]
    ):

    path_files_filtered = [
        os.path.join(path_current_dir, file) 
        for path_current_dir, _, files in os.walk(path_dataset) 
        for file in files 
        if any(
            file.endswith(file_extension) 
            for file_extension in filter_file_ext
        )
    ]
    
    return path_files_filtered

def join_metadata_files():

    paths_metadata  = get_all_files_in_path_filtered_by_extesion(
        "./src/ebeer_dataset/", ["json"]
    )

    json_content_arr = []
    for path_metadata in paths_metadata:
        # print('path_metadata:', path_metadata)
        with open(path_metadata, 'r') as file:
            file_content = json.load(file)
            # print('file_content:', file_content, '\n')
            json_content_arr.append(file_content)

    with open("src/artifacts/general_metadata.json", "w") as file_writer:
        json.dump(json_content_arr, file_writer)

def execute_data_augmentation():

    paths_dataset_images = get_all_files_in_path_filtered_by_extesion(
        "./src/ebeer_dataset/", [".jpg", ".png"]
    )

    # for path_file in paths_dataset_images:
    #     execute_data_augmentation_operation_on_image_by_path(path_file)

if __name__ == "__main__":

    print('\n')

    join_metadata_files()

    # execute_data_augmentation()

    print('\n')
