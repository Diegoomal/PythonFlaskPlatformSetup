import os
import mlflow


MLFLOW_TRACKING_USERNAME = 'diego.maldonado'
MLFLOW_TRACKING_PASSWORD = 'd431b7b196e28028b386d497062f5ecad26855ed'
MLFLOW_TRACKING_URI = 'https://dagshub.com/diego.maldonado/'
+ 'proj_integrado_cnn_cerveja.mlflow'

os.environ['MLFLOW_TRACKING_USERNAME'] = MLFLOW_TRACKING_USERNAME
os.environ['MLFLOW_TRACKING_PASSWORD'] = MLFLOW_TRACKING_PASSWORD

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

mlflow.tensorflow.autolog(log_models=True,
                            log_input_examples=True,
                            log_model_signatures=True)