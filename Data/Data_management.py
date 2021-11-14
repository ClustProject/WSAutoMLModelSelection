#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import os, sys


# In[3]:


class DataManagement:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def editData(inData):
        # to aviod error
        try:
            inDf = pd.read_csv(inData,encoding='ms949')  # get requested file
        except Exception as e :
            inDf = open(inData, 'rt', encoding = 'UTF-8')
            inDf = inDf.fillna("NaN")

            model, method = model_selection.getModel(uid, inSelectedModel, dataframe, window_size)
            inDf.close()
        return inDf

    def saveData(inData):  # request file to user 보내주는부분
        uid = inData  # get requested uid 받아오는 부분
        model, method = getModel(uid)
        result_df = model.df.copy()
        result = model.predict_result()
        if method == "NAOMI":
            result = model.scaler.inverse_transform(result.reshape(-1,1)).squeeze()
        result_df["value"] = result
        src = "media/result_" + uid + ".csv"
        result_df.to_csv(src, encoding='UTF-8')


# In[ ]:





# In[ ]:




