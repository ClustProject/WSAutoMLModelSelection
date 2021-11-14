#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os, sys
data_path = '../Data/__init__.py'
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(data_path))))
from Data.Data_management import editData


# In[4]:


class Analysis:
    def Analysis(inAnal):
        inAnal = editData()
        return outAnal


# In[ ]:




