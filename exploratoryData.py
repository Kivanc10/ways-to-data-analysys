# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 01:42:55 2020

@author: Kivanc
"""

#%%
import pandas as pd
data=pd.read_csv("pokemon.csv")
print(data.columns)
print(data["Type 1"].value_counts(dropna=False))
#dropna=False enable to see none elements.
print(data.describe())
#it is show us that higher or lower from rest of data.

#%%
#visual-exploratory of data
import matplotlib.pyplot as plt
data.boxplot(column="Attack",by="Legendary")
data.boxplot(column="Speed",by="Legendary")
#compare attack or speed skilss of pokemon that are legendary or not 



