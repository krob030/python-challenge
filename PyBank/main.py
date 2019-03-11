#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import glob
import os


# In[2]:


csv_path= "C:/Users/karsa_000/Desktop/budget_data.csv"


# In[14]:


budget_pd= pd.read_csv(csv_path)


# In[15]:


budget_pd.columns = ["Date", "Profit_Loss"]


# In[16]:


TotMonths= budget_pd["Date"].count()


# In[17]:


Total= budget_pd["Profit_Loss"].sum()


# In[18]:


Avg= budget_pd["Profit_Loss"].mean()


# In[19]:


Great_Inc= budget_pd.max()


# In[20]:


Great_Dec= budget_pd.min()


# In[21]:


title= ("Financial Analysis")
spaces= ("----------------------------")
print(title)
print(spaces)
print("Total Months: " + str(TotMonths))
print("Average  Change: " + str(Avg))
print("Greatest Increase in Profits: " + str(Great_Inc.to_string(header= None, dtype=None)))
print("Greatest Decrease in Profits: " + str(Great_Dec.to_string(header= None, dtype=None)))

