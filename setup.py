import io
import os
from pathlib import Path
from setuptools import find_packages,setup

#METADTA

NAME="prediction_models"
DESCRIPTION="Loan Prediction Model"
URL="https://github.com/Nithin-Bandi"
AUTHOR="Nithin"
EMAIL="125156022@sastra.ac.in"
REQUIRES_PYTHON=">=3.7.0"

#Present working dirctory
pwd=Path(os.path.abspath(os.path.dirname(__file__)))

#Get the list packages to be installed
def list_reqs(fname="requirements.txt"):
    with io.open(os.path.join(pwd,fname),encoding='utf-8') as file:
        return file.read().splitlines()
    

try:
    with io.open(os.path.join(pwd,'README.md'),encoding='utf-8') as file:
        long_description="\n"+file.read()
except FileNotFoundError:
    long_description=DESCRIPTION

ROOT_DIR=Path(__file__).resolve().parent
PACKAGR_DIR=ROOT_DIR/NAME
about={}
with open(PACKAGR_DIR/'VERSION') as file:
    _version=file.read().strip()
    about['__version__']=_version


setup(  
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={"prediction_model":['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True

)