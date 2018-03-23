
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


# ### reviews.csv
# 
# Summary Review data and Listing ID (to facilitate time based analytics and visualisations linked to a listing).

# In[59]:


reviews = pd.read_csv('airbnb_data/reviews.csv')
print(reviews.shape)
reviews.head(3)


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


# ### listings.csv
# 
# Summary information and metrics for listings in Edinburgh (good for visualisations).

# In[31]:


listings = pd.read_csv('airbnb_data/listings.csv')
print(listings.shape)
listings.head(1)


# In[34]:


for col in listings.columns:
    print(col)


# ### listings 2.csv 
# 
# Detailed Listings data for Edinburgh

# In[26]:


listings2 = pd.read_csv('airbnb_data/listings 2.csv')
print(listings2.shape)
listings2.head(1)


# In[30]:


for col in listings2.columns[:5]:
    print(col)

