#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
f = open('seoul.csv','rt',encoding='utf8')
data = csv.reader(f)
for row in data :
    print(row)
f.close()


# import csv
# f = open('seoul.csv', encoding = 'utf8')
# data = csv.reader(f)
# header = next(data)
# print(header)
# f.close()

# In[8]:


import csv
f = open('seoul.csv', encoding = 'utf8')
data = csv.reader(f)
header = next(data)
for row in data :
    print(row)
f.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




