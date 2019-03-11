#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import glob
import os


# In[14]:


csv_path= "C:/Users/karsa_000/Desktop/election_data.csv"


# In[17]:


election_pd= pd.read_csv(csv_path)


# In[18]:


election_pd.columns = ["Voter ID", "County", "Candidate"]


# In[19]:


TotVote= election_pd["Voter ID"].count()


# In[20]:


name= str(election_pd["Candidate"].unique())
print(name)


# In[21]:


title= ("Election Results")
spaces= ("----------------------------")
print(title)
print(spaces)
print("Total Votes: " + str(TotVote))
print(spaces)
print(name)
print(spaces)
print(spaces)

