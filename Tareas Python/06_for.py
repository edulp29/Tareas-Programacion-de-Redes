#!/usr/bin/env python
# coding: utf-8

# In[7]:


Names=['Joe', 'Jack', 'Tony', 'Paul', 'George']
Selected=[]
print(Names)
for element in Names:
    print("El nombre en esta posicion es:",element)
for element in Names:
    if "a" in element:
        Selected.append(element)
print(Selected)


# In[ ]:




