# -*- coding: utf-8 -*-
#%%
import pandas as pd

data=pd.read_csv("pokemon.csv")
print(data.head())
print(data.tail())
print(data.columns)
print(data.shape)
print(data.info())

