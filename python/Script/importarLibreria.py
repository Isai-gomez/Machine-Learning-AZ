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
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values