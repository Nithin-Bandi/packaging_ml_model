import os
import sys
from prediction_models.config import config
with open(os.path.join(config.PACKAGE_ROOT,'VERSION')) as file:
    __version__=file.read().strip()