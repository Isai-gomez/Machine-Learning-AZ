#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:00:10 2020

@author: chia
"""
# Plantilla de pre procesado

# Cómo importar las librerias
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# importar el data set
dataset = pd.read_csv("../datasets/Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

#Tratamiento NAs
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

#Codificar datos categoricos X
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder 
from sklearn.compose import ColumnTransformer
let_X = preprocessing.LabelEncoder()
X[:,0] = let_X.fit_transform(X[:,0])
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'),[0])],remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float)
#Codificar datos categoricos en Y
labelencoder_y = preprocessing.LabelEncoder()
y = labelencoder_y.fit_transform(y)
