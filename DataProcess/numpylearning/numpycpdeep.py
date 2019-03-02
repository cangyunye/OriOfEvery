
# coding: utf-8

# In[1]:


import numpy as np
a = np.array([1,2,3,4])
b = a #b指向与a相同的一块内存
print(a)
print(b)
print(id(a),id(b))#查看内存地址
b is a


# In[2]:


a[0]=0.3
print(a)


# In[3]:


a[2]=2.8
print(a)


# a 与 b由于代指同一块内存，故同步变化

# In[4]:


print(b[1:3])
a[1:3]=[22,33]
print(b)


# 仅给c赋予a的值

# In[5]:


c = a.copy()
a[0]=5
print(c)
print(b)

