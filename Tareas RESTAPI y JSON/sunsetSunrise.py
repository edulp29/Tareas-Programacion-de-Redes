#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[27]:


latitud=43.3713
longitud=-8.396
url=("https://api.sunrise-sunset.org/json?lat=43.3713&lng=-8.396")
json_data= requests.get(url).json()
print(json_data)
print("La latitud de A Coruña es:",latitud,"y la longitud es:",longitud,".")
print("El sol sale a las:",(json_data["results"]["sunrise"]),"y se oculta a las:",(json_data["results"]["sunset"]),".")


# In[ ]:





# In[ ]:





# In[ ]:




