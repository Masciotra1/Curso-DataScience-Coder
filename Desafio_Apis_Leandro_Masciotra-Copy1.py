#!/usr/bin/env python
# coding: utf-8

# Me eh encontrado que muchos de los APIs  que eh probado no han funcionado.. y me queda la duda si realmente seguian en vigencia desde la pagina que los ofrecia.
# elegi el mismo que fue usado en clases... me ubiese gustado poder aplicar alguno que sea relacionado a los servicios de salud pero los que eh  probado no han funcionado...
# 

# In[15]:


import requests
import json
import pandas as pd

url = "https://datosabiertos-usig-apis.buenosaires.gob.ar/datos_utiles?x=98725&y=100080&calle=CABILDO%20AV.&altura=1500"
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")


# In[16]:


response.text


# In[17]:


texto = response.text
jsondata = json.loads(texto)
df3 = pd.DataFrame([jsondata])
df3.head()


# In[ ]:




