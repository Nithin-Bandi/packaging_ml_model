from pathlib import Path
import os
import sys
PACKAGE_ROOT=Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))
import joblib
import pandas as pd
import prediction_models
from prediction_models.config import config
import prediction_models.preprocessing.data_handling as dh
import numpy as np
import sys
import pathlib
import prediction_models

classification_pipeline=dh.load_pipeline()


def generate_predictions(data_input):
    data=pd.DataFrame(data_input)
    pred=classification_pipeline.predict(data[config.FEATURES])
    output=np.where(pred==1,'Y','N')

    result= {"Predictions":output}
    return result


# def generate_predictions():
#     test_data=dh.load_datset(config.TEST_FILE)
#     pred=classification_pipeline.predict(test_data[config.FEATURES])
#     output=np.where(pred==1,'Y','N')
#     print(output)
#     return output

if __name__=='__main__':
    generate_predictions()