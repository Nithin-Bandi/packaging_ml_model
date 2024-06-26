from pathlib import Path
import os
import sys
PACKAGE_ROOT=Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))
from sklearn.pipeline import Pipeline
from prediction_models.config import config
import prediction_models.preprocessing.preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

classification_pipeline=Pipeline(
    [
       
        ("Mean Imputation",pp.Mean_Imputer(variables=config.NUM_FEATURES)),
        ("Mode Imputation",pp.Mode_Imputer(variables=config.CAT_FEATURES)),
        ("DomainProcessing",pp.DomainProcessing(variable_to_modify=config.FEATURES_TO_MODIFY,variable_to_add=config.FEATURE_TO_ADD)),
        ("Drop Columns",pp.DropColumns(variables_to_drop=config.DROP_FEATURES)),
        ("Label Encoder",pp.CustomLabelEncoder(variables_encode=config.FEATURES_TO_ENCODE)),
        ("Log Transform",pp.CustomLogTransform(variable_to_transform=config.LOG_FEATURES)),
        ("MinMaxScaller",MinMaxScaler()),
        ("LogisticClassifier",LogisticRegression(random_state=0))

    ]
)
