import os
import pandas as pd
import joblib
from prediction_models.config import config
import pathlib
import sys
import prediction_models
PACKAGE_ROOT=pathlib.Path(prediction_models.__file__).resolve().parent
sys.path.append(str(PACKAGE_ROOT))

def load_datset(file_name):
    filepath=os.path.join(config.DATA_PATH,file_name)
    _data=pd.read_csv(filepath)
    return _data

#SERILIZATION
def save_pipeline(pipeline_to_save):
    save_path=os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)  
    joblib.dump(pipeline_to_save,save_path) 
    print(f"Model has been saved under the name{config.MODEL_NAME}")

#DEDERILIZATION
def load_pipeline():
    save_path=os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)  
    model_loaded=joblib.load(save_path) 
    print(f"Model has been loaded ")
    return model_loaded
    

