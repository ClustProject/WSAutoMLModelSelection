#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import os


# In[20]:


# 해당 경로에 있는 .csv 파일명 리스트 가져오기
path = './'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .csv인 경우


# In[3]:


def editData(inData):
    inDf = pd.read_csv(inData,encoding='ms949')
    return inDf

