from sklearn.base import BaseEstimator,TransformerMixin
from prediction_models.config import config
import numpy as np
import pathlib
import sys
import prediction_models
PACKAGE_ROOT=pathlib.Path(prediction_models.__file__).resolve().parent
sys.path.append(str(PACKAGE_ROOT))
class Mode_Imputer(BaseEstimator,TransformerMixin):
    def __init__(self,variables=None):
        self.variables=variables
    
    def fit(self,X,y=None):
        self.mode_dict={}
        X=X.copy()
        for col in self.variables:
            
            self.mode_dict[col]=X[col].mode()[0]
        return self
    def transform(self,X):
        X=X.copy()
        for col in  self.variables:
            X[col].fillna(self.mode_dict[col],inplace=True)
        return X

class Mean_Imputer(BaseEstimator,TransformerMixin):
    def __init__(self,variables=None):
        self.variables=variables
    def fit(self,X,y=None):
        self.mean_dict={}
        X=X.copy()
        for col in self.variables:
            self.mean_dict[col]=X[col].mean()
        return self
    def transform(self,X):
        X=X.copy()
        for col in  self.variables:
            X[col].fillna(self.mean_dict[col],inplace=True)
        return X
    def fit_transform(self,X,y=None):
        self.fit(X,y)
        return self.transform(X)
        
        

class DropColumns(BaseEstimator,TransformerMixin):
    def __init__(self,variables_to_drop=None):
        self.variables_to_drop=variables_to_drop
    
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        X=X.copy()
        X.drop(self.variables_to_drop,axis=1,inplace=True)
        return X
    def fit_transform(self,X,y=None):
        self.fit(X,y)
        return self.transform(X)
        
        
class DomainProcessing(BaseEstimator,TransformerMixin):
    def __init__(self,variable_to_modify=None,variable_to_add=None):
        self.variable_to_modify=variable_to_modify
        self.variable_to_add=variable_to_add
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        X=X.copy()
        X[self.variable_to_modify]=X[self.variable_to_modify]+X[self.variable_to_add]
        return X
    def fit_transform(self,X,y=None):
        self.fit(X,y)
        return self.transform(X)

    
class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables_encode):
        self.variables_encode = variables_encode
        
    def fit(self, X, y=None):
        self.label_dict = {}
        X=X.copy()
        for var in self.variables_encode:
            t = X[var].value_counts().sort_values(ascending=True).index
            self.label_dict[var] = {k: i for i, k in enumerate(t, 0)}
        return self
    
    def transform(self, X):
        X = X.copy()
        for var in self.variables_encode:
            X[var] = X[var].map(self.label_dict[var])
        return X

    def fit_transform(self,X,y=None):
        self.fit(X,y)
        return self.transform(X)


class CustomLogTransform(BaseEstimator,TransformerMixin):
    def __init__(self,variable_to_transform):
        self.variable_to_transform=variable_to_transform

    def fit(self,X,y=None):
        return self
    def transform(self,X):
        X=X.copy()
        for var in self.variable_to_transform:
            X[var]=np.log(X[var])
        return X
    def fit_transform(self,X,y=None):
        self.fit(X,y)
        return self.transform(X)

class see_data(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        print(X.info())
        return X
