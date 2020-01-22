# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 02:42:56 2020

@author: Kivanc
"""

#%%
#plot,subplots,histogram
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("pokemon.csv")
data1=data.loc[:,["Attack","Defense","Speed"]]
print(data1)
data1.plot() #it is confusing
#%%
data1.plot(subplots=True)
#it divide all graphics to easy understand
plt.show()
#%%
data1.plot(kind="scatter",x="Attack",y="Defense")
plt.show()

data1.plot(kind="hist",y="Defense",bins=50,range=(0,250),normed=True)

fig,axes=plt.subplots(2,1) # we create two empty graphics.
data1.plot(kind="hist",y="Defense",bins=50,range=(0,250),ax=axes[0])
data1.plot(kind="hist",y="Defense",bins=50,range=(0,250),ax=axes[1],cumulative=True)
plt.show()
#range functions about x axes.
#bins counts of rectangles.
#cumulative means that add values to each when continue





