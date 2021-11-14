#!/usr/bin/env python
# coding: utf-8

# # 1. 라이브러리 선언

# In[8]:


import sys,os
import pandas as pd
import numpy as np

# 시계열 데이터 보간 모듈 패키지 추가
# from Preprocessing.NAOMI.naomi import NAMOIimputation
# from Preprocessing.BRITS.brits import BRITSimputation




# ,py파일 패키지 모듈 추가

from Visualization.Visualize import Visualize
from Analysis.Analysis import Analysis
from Data import Data_management
import Preprocessing


# In[9]:


class Model_selection:
    modelDic = {}
    def __init__(self, dataframe = None, model = None, uid = None):
        self.dataframe = dataframe
        self.model = model
        self.result= None
        self.uid = uid
    #보간 방법을 auto로 설정했을 때 모델을 자동으로 선택해주는 함수
    #연속되는 구간의 길이가 10 이상이라면 True, 아니면 False를 return 한다.
    def autoFind(dataframe):
        maxnull = 0
        cur = 0
        #dataframe을 순회하면서 NaN이 연속으로 나오는 횟수의 최댓값을 계산한다.
        for i in range(len(dataframe)):
            if dataframe["value"].iloc[i] == "NaN" or pd.isnull(dataframe["value"].iloc[i]):
                cur += 1
                maxnull = max(maxnull, cur)
            else:
                cur = 0
        return maxnull>10
    
    
    #모델들의 학습 상태를 저장할 dictionary
    #key: 세션의 고유한 id
    #value: (model, 모델종류 이름) 형태의 튜플
    
    def getModel(uid, inSelectedModel=None, dataframe = None, window_size = None):
        # uid: 요청을 보내온 세션의 고유한 id
        # inSelectedModel: 요청을 보내온 모델 종류
        
        #만약 uid가 modelDic에 존재한다면 그 그값을 return 한다.
        if uid in modelDic:
            return modelDic[uid]
        
#         if inSelectedModel == "TrainedModel":
#             TrainedModel(inModel)
        if inSelectedModel == "Analysis":
            analData = Analysis.Analysis
            
        elif inSelectedModel == "Preprocessing":
            preData = Preprocessing.Preprocessing
            
            #inSelectedModel이 NAOMI라면 NAOMI모델을, BRITS라면 BRITS모델을, 둘다 아니라면 자동으로 모델을 찾아서 모델을 생성한다.
            #모델을 생성한 후 uid를 key 값으로 modelDic에 넣는다.
            if inSelectedModel=="NAOMI":
                modelDic[uid] = (NAMOIimputation(dataframe = dataframe, window_size=window_size), "NAOMI")
                
            elif inSelectedModel=="BRITS":
                modelDic[uid] = (BRITSimputation(dataframe = dataframe), "BRITS")
                
            else:
                find = autoFind(dataframe)
                
                if find:
                    modelDic[uid] = (NAMOIimputation(dataframe = dataframe, window_size=len(dataframe)//10), "NAOMI")
                    
                else:
                    modelDic[uid] = (BRITSimputation(dataframe = dataframe), "BRITS")
#                     print(modelDic)

            #결과를 return한다.
            return modelDic[uid]
                
        elif inSelectedModel == "Visualization":
            visualData = Visualize.Visualize


# In[ ]:





# In[44]:


# print(os.getcwd())


# In[7]:


sys.path


# In[ ]:




