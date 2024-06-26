from pathlib import Path
import os
import sys
PACKAGE_ROOT=Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))
import pandas as pd
import numpy as np
from prediction_models.config import config
import prediction_models.preprocessing.data_handling as dh
import prediction_models.preprocessing.preprocessing as pp
import prediction_models.pipeline as pipe
import pathlib
import sys


def perform_training():
    train_data=dh.load_datset(config.TRAIN_FILE)
   # train_data.dropna(inplace=True)
    train_y=train_data[config.TARGET].map({'N':0,'Y':1})
    pipe.classification_pipeline.fit(train_data[config.FEATURES],train_y)
    dh.save_pipeline(pipe.classification_pipeline)

    
    
if __name__=="__main__":
    perform_training()

