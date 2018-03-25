
# coding: utf-8

# # Generation Rent Hackaton - Team Anorak
# 
# ## Analysis of Airbnb Data

# In[2]:


import pandas as pd


# ## The datasets:

# ### reviews 2.csv
# 
# Detailed Review Data for listings in Edinburgh

# In[3]:


reviews2 = pd.read_csv('airbnb_data/reviews 2.csv')
print(reviews2.shape)
reviews2.head(3)


# ### neighbourhoods.geojson
# 
# GeoJSON file of neighbourhoods of the city.

# In[4]:


neighbourhoods_geo_json = pd.read_json('airbnb_data/neighbourhoods.geojson')
print(neighbourhoods_geo_json.shape)
neighbourhoods_geo_json.head(3) # neighbourhood_group is all NaN


# ### neighbourhoods.csv
# 
# Neighbourhood list for geo filter. Sourced from city or open source GIS files.

# In[5]:


neighbourhoods = pd.read_csv('airbnb_data/neighbourhoods.csv')
print(neighbourhoods.shape)
neighbourhoods.head(3) # neighbourhood_group is all NaN


# ### calendar.csv
# 
# Detailed Calendar Data for listings in Edinburgh

# In[6]:


calendar = pd.read_csv('airbnb_data/calendar.csv')
print(calendar.shape)
calendar.head(3)


# ### listings 2.csv 
# 
# Detailed Listings data for Edinburgh

# In[7]:


listings2 = pd.read_csv('airbnb_data/listings 2.csv')
print(listings2.shape)
listings2.head(1)


# In[8]:


listings2['zipcode'].head()


# In[9]:


count = 0
for row in listings2['zipcode']:
    if len(str(row).split()) == 2:
        count += 1
print(count)


# In[10]:


for col in listings2.columns:
    print(col)


# In[11]:


listings2['neighbourhood'].value_counts()


# In[12]:


listings2['zipcode'].map(lambda x: str(x).split(' ')[0]).value_counts()[:3]


# ## EDA

# In[13]:


df = pd.read_csv('simd2016_withinds.csv')
deprivation = df[df['Council_area'] == 'City_of_Edinburgh']
deprivation.head()


# In[14]:


deprivation.shape


# In[15]:


simd16 = pd.read_csv('simd16.csv')
simd16.head()


# In[16]:


simd16.shape


# ## main deprivation df

# In[17]:


deprivation_all = pd.merge(simd16, deprivation, left_on='DZ', right_on='Data_Zone', how='right')
print(deprivation_all.shape)
deprivation_all.head()


# Merging deprivation with listings

# In[18]:


df_all = pd.merge(listings2, deprivation_all, left_on='zipcode', right_on='Postcode', how='left')
print(listings2.shape)
print(deprivation_all.shape)
print(df_all.shape)
df_all[['zipcode', 'Postcode']].head(10)


# In[19]:


df_all.drop_duplicates()


# In[22]:


from sklearn.dummy import DummyRegressor


# In[23]:


model = DummyRegressor()


# In[26]:


from sklearn.datasets import make_regression


# In[27]:


X, y = make_regression(n_samples=500, n_features=2)


# In[29]:


model.fit(X, y)


# In[32]:


len(model.predict(X))

