#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas_datareader import data as wb

MSFT_DATA = wb.DataReader('MSFT', 'yahoo', ('2000/1/1'))


# In[2]:


MSFT_DATA.head()


# In[3]:


MSFT_DATA.tail()


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


MSFT_DATA['Simple Rates Of Return'] = (MSFT_DATA['Adj Close']/MSFT_DATA['Adj Close'].shift(1)) - 1


# In[6]:


MSFT_DATA['Simple Rates Of Return'].tail()


# In[7]:


sror_msft = MSFT_DATA['Simple Rates Of Return'].plot(figsize=(8,5))


# In[8]:


average_r_d = MSFT_DATA['Simple Rates Of Return'].mean()


# In[9]:


average_r_d


# In[10]:


average_r_a = MSFT_DATA['Simple Rates Of Return'].mean()*250 #250 trading days in a year
average_r_a


# In[11]:


avg_r_a = str(round(average_r_a, 5)* 100) + '%'


# In[12]:


avg_r_a

