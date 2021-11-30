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
# 학습 완료한 딥러닝 모델 pickle 파일로 변환
import pickle
import joblib

def create_pkl_file(inAnal):
    filename = "anal_result.pkl"
    # 변수 저장 기반 예측
    saved_model = pickle.dumps(Analysis.Analysis(inAnal))
    # Load the pickled model
    analsys_from_pickle = pickle.loads(saved_model)

    # Use the loaded pickled model to make predictions
    analsys_from_pickle.predict("predictVal")
    
    # 파일 저장 기반 예측
    joblib.dump(Analysis.Analysis(inAnal), filename)
    clf_from_joblib = joblib.load(filename) 
    clf_from_joblib.predict("predictVal")



