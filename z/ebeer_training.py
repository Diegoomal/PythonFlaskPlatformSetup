
"""# Obtenção da base de dados"""

# !git clone https://github.com/Diegoomal/ebeer_dataset.git

"""# Importação dos modulos necessários"""

import os
from os import listdir
from os.path import isfile, join
import cv2
import PIL
import random
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import mlflow

import tensorflow as tf
tf.config.run_functions_eagerly(True)

from adabelief_tf import AdaBeliefOptimizer
from sklearn.model_selection import train_test_split

from datetime import datetime
import random as python_random
from tensorflow import keras
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import VGG16
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import (Activation, Dropout, Dense, Flatten,
                                     BatchNormalization, Conv2D, MaxPooling2D,
                                     Input, AveragePooling2D)
from keras.callbacks import ReduceLROnPlateau, LearningRateScheduler

"""# Configuração do MLflow"""

MLFLOW_TRACKING_USERNAME = 'diego.maldonado'
MLFLOW_TRACKING_PASSWORD = 'd431b7b196e28028b386d497062f5ecad26855ed'
MLFLOW_TRACKING_URI = 'https://dagshub.com/diego.maldonado/proj_integrado_cnn_cerveja.mlflow'

os.environ['MLFLOW_TRACKING_USERNAME'] = MLFLOW_TRACKING_USERNAME
os.environ['MLFLOW_TRACKING_PASSWORD'] = MLFLOW_TRACKING_PASSWORD

# mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

# mlflow.tensorflow.autolog(log_models=True,
#                           log_input_examples=True,
#                           log_model_signatures=True)

"""# Definição de funções adicionais"""

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
   np.random.seed(123) 
   python_random.seed(123)
   tf.random.set_seed(1234)

"""# Leitura do dataset e atribuição às respectivas variáveis"""

width = 128
height = 128
channels = 3

size = (height, width)

datasetPath = 'ebeer_dataset'

filePath = '0'
filesname = read_files_names(datasetPath, filePath)
filesname.remove("metadata.json")
imgs = [read_image(datasetPath, filePath, filename) for filename in filesname]
train_data_skol = [np.array(image).astype('float32')/255 for image in imgs]
# print("train_data_skol:", len(train_data_skol))

filePath = '1'
filesname = read_files_names(datasetPath, filePath)
filesname.remove("metadata.json")
imgs = [read_image(datasetPath, filePath, filename) for filename in filesname]
train_data_brahma = [np.array(image).astype('float32')/255 for image in imgs]
# print("train_data_brahma:", len(train_data_brahma))

filePath = '2'
filesname = read_files_names(datasetPath, filePath)
filesname.remove("metadata.json")
imgs = [read_image(datasetPath, filePath, filename) for filename in filesname]
train_data_heiniken = [np.array(image).astype('float32')/255 for image in imgs]
# print("train_data_heiniken:", len(train_data_heiniken))

"""# Separação do dataset em treino e teste"""

labels_index = {    
     0: "skol"
  ,  1: "brahma"
  ,  2: "heiniken"
}

n_neuronios_saida = len(labels_index)

train_data_X = np.concatenate(
    (
        train_data_skol
        , train_data_brahma
        , train_data_heiniken
    )
)

train_data_y = to_categorical(
    np.concatenate(
        (
              np.zeros(len(train_data_skol)) # * 0
            , np.ones(len(train_data_brahma)) # * 1
            , np.ones(len(train_data_heiniken)) * 2
        )
    )
)

X_train, X_test, y_train, y_test = train_test_split(
  # train_data_X, train_data_y,
  tf.convert_to_tensor(train_data_X), tf.convert_to_tensor(train_data_y),
  test_size=0.3, random_state=42)

"""# Modelagem e compilação"""

learning_rate = 1e-4
adam_optimizer = Adam(learning_rate=learning_rate)

reset_seeds()

model = Sequential()

# Extração de caracteristicas
model.add(Conv2D(256, (3, 3), activation='relu',
    input_shape=(width, height, channels)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D( 64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D( 32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

# Achatamento
model.add(Flatten())

# classificadores
model.add(Dense(128, activation='relu'))
model.add(Dense( 64, activation='relu'))
model.add(Dense(  n_neuronios_saida, activation='softmax'))

model.compile(
  optimizer=Adam(learning_rate=learning_rate), loss='binary_crossentropy',
  metrics=['accuracy', tf.keras.metrics.Precision(), tf.keras.metrics.Recall()]
)

"""# Execução do treino do modelo"""

# Commented out IPython magic to ensure Python compatibility.

# with mlflow.start_run(run_name='cnn_img_beer'):
#   reset_seeds()
#   hist = model.fit(X_train, y_train, epochs=25, validation_split=0.2)
#   model.evaluate(X_test, y_test)

hist = model.fit(X_train, y_train, epochs=25, validation_split=0.2)

"""# Predição com o modelo treinado"""

from IPython.display import Image

def predic_img(i):

  image_path = f'assets/{i}.jpg'
  
  image_original = tf.keras.utils.load_img(
      image_path,
      grayscale=False, 
      color_mode='rgb', 
      target_size=None, 
      interpolation='nearest'
  )

  image_resized = image_original.resize(size)

  image_prepared = np.expand_dims(image_resized, axis=0)

  prediction = model.predict(image_prepared)

  display(Image(image_path, width=50, height=50))

  n_pos = prediction.argmax(axis=-1)[0]
  
  print(
      'Prediction for item:', i
      , '- position:', n_pos
      , ' - label:', labels_index[n_pos]
      , '\n\n'
  )

# predic_img('0')

# for i in range(0, 20):
#   predic_img(i)

"""# Salvar o modelo no google drive"""

model.save('/src/model/cnn_trained_model_beer.h5')