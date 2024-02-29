#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


maths = np.array([82,88,90,75,70])
maths


# In[4]:


physics = np.array([80,79,85,92,86])
physics


# In[6]:


chemistry = np.array([90,80,87,78,89])
chemistry


# In[7]:


total = maths + physics + chemistry
total


# In[8]:


#normal array created without numpy
x= ([10,20,30,40,50])
x**2


# In[10]:


total /300 *100


# In[3]:


#we can perform operation in the array with the help of numpy
x =np.array([5,6,10,12,34,23,14])
y = np.array([2,3,4,2,4,3,5])
x**y


# In[8]:


#we can perform operation in the array with the help of numpy
#the number of the elements of both the array should be same
x =np.array([5,6,10,12,34,23,14])
y = np.array([2,3,4,2,4,3,5])
x**y,x/y,x//y,x%y


# In[9]:


type(x)


# In[10]:


#use math library
import math as m


# In[11]:


#there is issue with math library is that is works with scaler data type of only
m.log10(x)


# In[12]:


#however we can use the numpy lib instance
np.log10(x),np.log2(x),np.sqrt(x),np.abs(x)


# In[13]:


#use of scaler value with math library
m.sin(m.radians(30))


# In[15]:


#with the numpy we can convert the following array into sin value
x = np.array([0,30,45,60,90])
np.sin(np.radians(x))


# In[18]:


np.sin(np.radians(x))**2 + np.cos(np.radians(x))**2


# In[19]:


x = iter(x)
type(x)


# In[22]:


#2-D Array
marks = np.array([[82,98,89,33,56,67],[90,89,87,67,78,99],[78,88,97,98,89,78]])
marks


# In[24]:


#ndim It tells you about the dimesion of the object
marks.ndim


# In[26]:


#.shape, Shape of the array
marks.shape

