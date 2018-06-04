
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


A = np.arange(12).reshape((3,4))
print(A)


# 按axis=1，纵向分割为2列

# In[3]:


print(np.split(A,2,axis=1))


# In[4]:


print(np.hsplit(A,2))


# 按axis=0，横向分割为3行

# In[5]:


print(np.split(A,3,axis=0))


# In[6]:


print(np.vsplit(A,3))


# 进行不等量分割1

# In[7]:


print(np.split(A,[1,1,2],axis=1))


# 进行不等量分割2

# In[8]:


print(np.array_split(A,3,axis=1))

