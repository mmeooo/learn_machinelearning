#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[2]:


# 파일 읽어 오기
pickle.load(open('./saves/favorite_save.pkl', 'rb'))


# In[3]:


favorite_load= pickle.load(open('./saves/favorite_save.pkl', 'rb'))
print(favorite_load) # 주피터로 써서 출력할 때 print써야함


# In[4]:


type(favorite_load)


# In[5]:


print(favorite_load['tiger']) # 주피터로 써서 출력할 때 print써야함


# In[7]:


# 파일이므로 open명령 써야함, binary형식의 파일모드는 'rb'
autompg_lr= pickle.load(open('./saves/autompg_lr.pkl', 'rb'))
print(autompg_lr) # 주피터로 써서 출력할 때 print써야함


# In[8]:


autompg_lr.predict([[3504.0, 8]])


# In[ ]:

a= 3504.0
b= 8
import numpy as np
pre= np.array([[a,b]])
print(autompg_lr.predict(pre))

print(autompg_lr.predict([[3504.0, 8]]))


