#!/usr/bin/env python
# coding: utf-8

# # Avocado database
# ## Librairies

# In[1]:


import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt


# ## Dataset

# In[2]:


avocat= pd.read_csv("avocats.csv",sep=",")


# In[3]:


avocat


# In[4]:


del avocat['Unnamed: 0'] 


# In[5]:


avocat


# In[6]:


avocat.columns


# In[7]:


nb_lignes, nb_col = avocat.shape
print(f"nb lignes : {nb_lignes}\nnb col : {nb_col}")


# In[8]:


avocat.dtypes


# ## Analyse

# In[26]:


# Total avocat par région
t1 = avocat.groupby("region").TotVolume.sum().sort_values()
t1.head()


# In[48]:


# Total avocat US
avocat.TotVolume.sum()


# #### Moyenne de prix par région 

# In[49]:


# Prix moyen sur les dernières années d'un avocat par région US
avocat.groupby("region").AveragePrice.mean().sort_values().tail()


# In[50]:


# Prix moyen sur les dernières années d'un avocat au US
avocat.AveragePrice.mean()


# In[15]:


plt.rcParams['figure.figsize'] = [15, 6] # Taille du graphique en pouces
plt.rcParams['figure.dpi'] = 200 # résolution en points par pouce
avocat[(avocat.region=="HartfordSpringfield")].groupby("Date").AveragePrice.mean().plot()
avocat[(avocat.region=="StLouis")].groupby("Date").AveragePrice.mean().plot()
avocat[(avocat.region=="Houston")].groupby("Date").AveragePrice.mean().plot()


# In[16]:


avocat[(avocat.region=="HartfordSpringfield")].groupby("Date").TotVolume.mean().plot()
avocat[(avocat.region=="StLouis")].groupby("Date").TotVolume.mean().plot()
avocat[(avocat.region=="Houston")].groupby("Date").TotVolume.mean().plot()


# #### Type d'avocat par région

# In[23]:


avocat[(avocat.region=="HartfordSpringfield")].groupby("Date").V4046.sum().plot()
avocat[(avocat.region=="HartfordSpringfield")].groupby("Date").V4225.sum().plot()
avocat[(avocat.region=="HartfordSpringfield")].groupby("Date").V4770.sum().plot()


# In[28]:


avocat[(avocat.region=="StLouis")].groupby("Date").V4046.sum().plot()
avocat[(avocat.region=="StLouis")].groupby("Date").V4225.sum().plot()
avocat[(avocat.region=="StLouis")].groupby("Date").V4770.sum().plot()


# In[44]:


avocat[(avocat.region=="Houston")].groupby("Date").V4046.sum().plot()
avocat[(avocat.region=="Houston")].groupby("Date").V4225.sum().plot()
avocat[(avocat.region=="Houston")].groupby("Date").V4770.sum().plot()


# #### Types d'avocats

# In[33]:


Type =avocat.pivot_table('TotVolume',index='Date',columns='type',aggfunc=sum)
Type.tail() #Tail = queue du tableau


# In[36]:


Type.plot(title="Type d'avocats")

