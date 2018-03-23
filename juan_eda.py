
# coding: utf-8

# # Generation Rent Hackaton - Team Anorak
# 
# ## Analysis of Airbnb Data

# In[1]:


import pandas as pd


# ## The datasets:

# ### reviews 2.csv
# 
# Detailed Review Data for listings in Edinburgh

# In[60]:


reviews2 = pd.read_csv('airbnb_data/reviews 2.csv')
print(reviews2.shape)
reviews2.head(3)


# ### neighbourhoods.geojson
# 
# GeoJSON file of neighbourhoods of the city.

# In[46]:


neighbourhoods_geo_json = pd.read_json('airbnb_data/neighbourhoods.geojson')
print(neighbourhoods_geo_json.shape)
neighbourhoods_geo_json.head(3) # neighbourhood_group is all NaN


# ### neighbourhoods.csv
# 
# Neighbourhood list for geo filter. Sourced from city or open source GIS files.

# In[42]:


neighbourhoods = pd.read_csv('airbnb_data/neighbourhoods.csv')
print(neighbourhoods.shape)
neighbourhoods.head(3) # neighbourhood_group is all NaN


# ### calendar.csv
# 
# Detailed Calendar Data for listings in Edinburgh

# In[37]:


calendar = pd.read_csv('airbnb_data/calendar.csv')
print(calendar.shape)
calendar.head(3)


# ### listings 2.csv 
# 
# Detailed Listings data for Edinburgh

# In[26]:


listings2 = pd.read_csv('airbnb_data/listings 2.csv')
print(listings2.shape)
listings2.head(1)


# In[61]:


for col in listings2.columns:
    print(col)


# In[104]:


listings2['neighbourhood'].value_counts()


# In[91]:


listings2['zipcode'].map(lambda x: str(x).split(' ')[0]).value_counts()[:3]


# ## EDA

# In[87]:


df = pd.read_csv('simd2016_withinds.csv')
deprivation = df[df['Council_area'] == 'City_of_Edinburgh']
deprivation.head()


# In[105]:


deprivation['Intermediate_Zone'].value_counts()


# In[117]:


deprivation.shape


# In[116]:


deprivation.head()


# In[118]:


simd16 = pd.read_csv('simd16.csv')
simd16.head()

