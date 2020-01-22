# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 02:09:36 2020

@author: Kivanc
"""

#%%
import pandas as pd
data=pd.read_csv("pokemon.csv")
print(data.dtypes)
#we will convert that data types each other
data["Type 1"]=data["Type 1"].astype("category")
data["Speed"]=data["Speed"].astype("float")
print(data.dtypes)

