#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import glob
import os


# In[7]:


csv_path= "C:/Users/karsa_000/Desktop/budget_data.csv"
csv_path


# In[8]:


budget_pd= pd.read_csv(csv_path)
budget_pd.head()


# In[43]:


Total_months= budget_pd.count()
print (Total_months)


# In[ ]:




