# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 02:12:31 2020

@author: Kivanc
"""

#%%
import pandas as pd
data=pd.read_csv("pokemon.csv")
print(data.info())
print(data["Type 2"].value_counts(dropna=False))
data1=data.copy()
data1["Type 2"].dropna(inplace=True)
data1["Type 2"].value_counts()
#we removed empty(nan) values using dropna functions
data2=data.copy()
data2["Type 2"].fillna("empty",inplace=True)
data2["Type 2"].value_counts()
#we renamed none values empty.

assert data2["Type 2"].notnull().all() 
#it is not returns none because it is true

