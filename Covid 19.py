#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# In[62]:


corona_dataset_csv = pd.read_csv("/Users/nava/Desktop/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head()
corona_dataset_csv.head(10)


# In[3]:


corona_dataset_csv.shape


# In[63]:


corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)
corona_dataset_csv.head(10)


# In[5]:


#Aggregating the rows by the country
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.head()


# In[6]:


corona_dataset_aggregated.shape


# In[7]:


# Visualizing data related to a country for example China
corona_dataset_aggregated.loc["China"].plot()


# In[8]:


corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc['Italy'].plot()
corona_dataset_aggregated.loc['Spain'].plot()
plt.legend()#hsoew the name of country color


# In[9]:


corona_dataset_aggregated.loc["China"].plot()


# In[10]:


corona_dataset_aggregated.loc["China"][:3].plot()#see in 3 dasy


# In[11]:


corona_dataset_aggregated.loc["China"].diff().plot()


# In[12]:


corona_dataset_aggregated.loc["China"].diff().max()


# In[13]:


#max rate in each country in the list
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for c in countries:
   max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
max_infection_rates


# In[14]:


corona_dataset_aggregated["max_infection_rate"] = max_infection_rates
corona_dataset_aggregated.head()


# In[15]:


corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])


# In[16]:


corona_data.head()


# In[80]:


happiness_report_csv = pd.read_csv("/Users/nava/Desktop/worldwide_happiness_report.csv")
happiness_report_csv.head()   


# In[83]:


useless_cols = ["Overall rank","Score","Generosity","Perceptions of corruption"]


# In[84]:


#derop method to remove the columns
happiness_report_csv.drop(useless_cols,axis=1,inplace=True)
happiness_report_csv.head()


# In[85]:


happiness_report_csv.set_index("Country or region",inplace=True)


# In[86]:


happiness_report_csv.head()


# In[87]:


corona_data.head()


# In[88]:


corona_data.shape


# In[89]:


happiness_report_csv.head()


# In[90]:


happiness_report_csv.shape


# In[92]:


#use inner use becuase both number of countries in both data sets are differernt
data = corona_data.join(happiness_report_csv,how="inner")
data.head()


# In[93]:


data.shape


# In[94]:


#correlation between max rate of corona and the other life columns
data.corr()


# In[95]:


#Visualization
data.head()


# In[96]:


#plotting GDP vs max infection rate
x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,y)


# In[97]:


#lets change the sacale for y to see the better plot
sns.scatterplot(x,np.log(y))


# In[98]:


sns.regplot(x,np.log(y))


# In[ ]:




