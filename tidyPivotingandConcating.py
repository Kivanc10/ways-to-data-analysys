# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 01:52:15 2020

@author: Kivanc
"""

#%%
import pandas as pd
data=pd.read_csv("pokemon.csv")
data_new=data.head()
print(data_new)
#we will melt this data
melted=pd.melt(frame=data_new,id_vars="Name",value_vars=["Attack","Defense"])

#we will pivot this data.Pivoting reverse of melting
pivoted=melted.pivot(index="Name",columns="variable",values="value")

#we will concatenate these datas
data1=data.head()
data2=data.tail()
concatenateData=pd.concat([data1,data2],axis=0,ignore_index=True)
print(concatenateData)
#ignore_index=index number is ignore.
# this method associate data to each other
#axis=0
#%%
data3=data["Attack"].head()
data4=data["Defense"].head()
conc_data=pd.concat([data3,data4],axis=1,ignore_index=True)
print(conc_data)




