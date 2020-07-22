#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
f = open('seoul.csv', encoding='utf8')
data = csv.reader(f)

for row in data :
    print(row)


# In[4]:


import csv
f = open('seoul.csv', encoding='utf8')
data = csv.reader(f)
next(data)

for row in data :
    print(row[-1])


# In[11]:


import csv
f = open('seoul.csv', encoding='utf8')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '':
        result.append(float(row[-1]))
print(result)
print(len(result))


# In[15]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', encoding='utf8')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '':
        result.append(float(row[-1]))
print(result)
print(len(result))
plt.figure(figsize = (10,2))
plt.plot(result, 'r')

plt.show()


# In[19]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', encoding='utf8')
data = csv.reader(f)
next(data)
result = []


for row in data :
    if row[-1] != '':
        if row[0].split('-')[1] == '08' :
            result.append(float(row[-1]))
print(result)
print(len(result))
plt.plot(result, 'r')

plt.show()


# In[20]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', encoding='utf8')
data = csv.reader(f)
next(data)
result = []


for row in data :
    if row[-1] != '':
        if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14':
            result.append(float(row[-1]))
print(result)
print(len(result))
plt.plot(result, 'r')

plt.show()


# In[1]:


import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', encoding='utf8')
data = csv.reader(f)
next(data)
high = []
low = []


for row in data :
    if row[-1] !='' and row[-2] !='' :
        if 1996 <= int(row[0].split('-')[0]) :
            if row[0].split('-')[1] == '09' and row[0].split('-')[2]=='04' :
                
                high.append(float(row[-1]))
                low.append(float(row[-2]))
plt.title('d안농')    
plt.plot(high, 'hotpink')
plt.plot(low, 'skyblue')
plt.show()


# In[ ]:





# In[ ]:




