# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 02:23:26 2020

@author: Kivanc
"""

#%%
# we will see to how occur dataFrames all over.
import pandas as pd
country=["Spain","France"] 
population=["50 b","60 b"]
data_label=["country","population"]
data_col=[country,population]
zipped=list(zip(data_label,data_col))
dictionary=dict(zipped)
df=pd.DataFrame(dictionary)
df["capital"]=["Madrid","Paris"]
#add new columns
df["point"]=0
#broadcasting entire columns


