#!/usr/bin/env python
# coding: utf-8

# The problem is to analyze commodity prices for various commodities using the commodity
# prices dataset. The goal is to leverage Python, data science techniques, statistical analysis
# and data modeling. Perform all necessary steps to get the key insights from the data.

# This dataset contains monthly commodity prices from 1960 to 2022. The commodity prices
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('commodity_prices (1) (1).csv')
df.head()


# ## EDA 

# In[6]:


df.shape


# In[9]:


# Dropping Unnamed column 
df = df.drop(columns = ['Unnamed: 0'])


# In[11]:


df.head(2)


# In[12]:


df.isnull().sum  # No Null Values / No action required 


# In[14]:


df.describe().T


# ####  if any null value
#   #1 -- droping the null value   
#   df=df.dropna()
#     
#   #2 -- filling the null values
# 
# 
# 
# #df=df["oil_dubai"].fillna(23.67)  # manualy
# 
# #df=df["oil_dubai"].fillna(x) where x is mean of the column

# In[15]:


df.info()


# In[16]:


# we have date in Object datattype so we have to chage it into datetime 

df['date'] = pd.to_datetime(df['date'],format = '%Y-%m-%d')


# In[17]:


df.info()


# #### 1. What is the maximum price of Robusta coffee ?

# In[19]:


df['coffee_robustas'].max()


# #### 2. What is the 75th percentile of sugar prices in the European Union (EU)?
#  

# In[24]:


sugar_eu_75 =  df["sugar_eu"].quantile(0.75)

sugar_eu_75                                      


# #### 3. What is the skewness of the price distribution for Arabica coffee?

# In[26]:


df['coffee_arabica'].skew() # therefore this data is right skew data 


# In[44]:


sns.lineplot(df['coffee_arabica'].head(20))


# #### Q4) Is the distribution of sugar prices in the US significantly different from a normal distribution?

# In[48]:


# null Hypothesis : normal distribution
# alternateHypothesis : not  normal distribution

 
from scipy import stats

us_sugar = df['sugar_us']
test,p = stats.normaltest(us_sugar)
print('p_value: ', p)

if p < 0.05:
    print('Reject Null hypothesis / not normally distributed ')
else:
    print('Failed to reject null/Accept null// normally distributed')




# #### 5. Which commodity experienced the highest price fluctuations during the observed period?

# In[49]:


# create a vairable with all the coulumns
# run a for loop and find Max()-Min() for each coulmn
# find the highest fluctuation value

df.columns


# In[65]:


a =[ 'oil_brent', 'oil_dubai', 'coffee_arabica', 'coffee_robustas',
       'tea_columbo', 'tea_kolkata', 'tea_mombasa', 'sugar_eu', 'sugar_us',
       'sugar_world']

l = []
for i in a:
    x = df[i].max() - df[i].min()
    l.append(x)

# Convert the two lists into a dictionary
result_dict = dict(zip(a, l))

print(result_dict)


# In[ ]:


# Therefore aximum fluctustion is in  oil_brent 


# #### 6 What is the overall price trend for each commodity ?

# In[67]:


plt.plot(df['oil_brent'])
plt.show


# In[ ]:




