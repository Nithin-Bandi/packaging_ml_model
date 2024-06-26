from pathlib import Path
import sys
import os
PACKAGE_ROOT=Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))


import pytest
from prediction_models.config import config
from prediction_models.preprocessing.data_handling import load_datset
from prediction_models.predict import generate_predictions

@pytest.fixture
def single_prediction():
    test_data=load_datset(config.TEST_FILE)
    single_row=test_data[:1]
    result=generate_predictions(single_row)
    return result

def test_single_prediction_not_none(single_prediction):
    assert single_prediction is not None
def test_single_prediction_is_string(single_prediction):
    assert isinstance(single_prediction.get('Predictions')[0],str)
def test_single_prediction_validate(single_prediction):
    assert single_prediction.get('Predictions')[0]=='Y'



