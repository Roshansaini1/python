#!/usr/bin/env python
# coding: utf-8

# In[5]:


string1=input("Write the sentence you want to convert into acronym: ")
string2=string1.split()
a=""
for word in string2:
    a += word[0]
a=a.upper()
print("Final Acronym of {} : {}".format(string1,a))


# In[ ]:





# In[ ]:




