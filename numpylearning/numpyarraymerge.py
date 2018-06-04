
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


A = np.array([1,1,1])
B = np.array([2,2,2])
print(A)
print(B)


# vstack，上下合并

# In[3]:


C = np.vstack((A,B)) #将A，B上下合并
print(C,C.shape)


# hstack，左右合并

# 补充一个维度，置于列位

# In[4]:


D = np.hstack((A,B)) #将A，B左右合并
print(D,D.shape)


# In[5]:


print(A[:,np.newaxis]) #补充一个维度


# 补充一个维度，置于行位

# In[6]:


print(A[np.newaxis,:]) #补充一个维度


# 重新设计为3行1列

# In[7]:


print(A.reshape(3,1)) 


# axis=0即上下维度合并

# In[8]:


E = np.concatenate((A,B,B,A),axis=0)
print(E)


# In[9]:


A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
print(A)
print(B)


# axis=1即横向维度合并

# In[10]:


F = np.concatenate((A,B,B,A),axis=1)
print(F)

