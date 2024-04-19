#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data=pd.read_excel("data.xlsx")
data


# In[6]:


data.isna()


# In[8]:


data.isna().sum()


# In[15]:


data.isna().sum().sum()


# In[24]:


data.columns


# In[ ]:





# In[19]:


data[data['Cuisines'].isna()==True]


# In[32]:


data.duplicated()


# In[33]:


data.duplicated().sum()


# In[34]:


data['City'].unique()


# In[36]:


data.City.nunique()


# In[38]:


data.columns


# In[42]:


data[['Restaurant ID','City']].groupby('City').nunique().sort_values('Restaurant ID')


# In[43]:


data['Restaurant Name'].value_counts()


# In[45]:


data[['Restaurant Name','Country Code']].groupby('Restaurant Name').nunique().sort_values('Country Code')


# In[46]:


data['Has Table booking'].value_counts()


# In[49]:


data['Has Table booking'].value_counts(normalize=True)*100


# In[54]:


data[['Has Online delivery','Votes']].groupby('Has Online delivery').sum()


# In[56]:


CityWise_Restaurant = data[['Restaurant ID','City']].groupby('City').nunique().sort_values('Restaurant ID')
CityWise_Restaurant


# In[ ]:





# In[ ]:





# In[ ]:





# In[74]:


City_Cuisines_1= data[['Restaurant ID', 'Restaurant Name', 'City','Cuisines']].copy()
City_Cuisines_1


# In[75]:


City_Cuisines_2= data[['Restaurant ID', 'Restaurant Name', 'City','Cuisines']].dropna().copy()
City_Cuisines_2


# In[76]:


City_Cuisines_2['Cuisines'] = City_Cuisines_2['Cuisines'].apply(lambda x : x.split(',') )


# In[77]:


City_Cuisines_2


# In[104]:


City_Cuisines_2['Number of Cuisines'] = City_Cuisines_2['Cuisines'].apply(lambda x : len(x) )
City_Cuisines_2


# In[105]:


City_Cuisines_2.sort_values('Number of Cuisines')


# In[80]:


City_Cuisines_2.explode('Cuisines')


# In[81]:


City_Cuisines_2.explode('Cuisines').head(20)


# In[83]:


City_Cuisines_Expanded =City_Cuisines_2.explode('Cuisines')
City_Cuisines_Expanded


# In[91]:


City_Cuisines_Expanded.sort_values(['City','Cuisines'])


# In[85]:


City_Cuisines_Expanded.groupby(['City','Cuisines']).count()


# In[93]:


City_Cuisines_Expanded_1 = City_Cuisines_Expanded.groupby(['City','Cuisines']).count()


# In[98]:


City_Cuisines_Expanded_1[['Restaurant ID']]


# In[98]:


City_Cuisines_Expanded_1[['Restaurant ID']]


# In[99]:


data['Price range'].value_counts()


# In[101]:


data['Price range'].value_counts(normalize=True)*100


# In[109]:


City_Cuisines_Expanded.groupby(['City','Cuisines']).count()[['Restaurant ID']].reset_index().sort_values(['City','Restaurant ID'],ascending=[True,False])


# In[ ]:




