#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,6,7,8,10])
plt.show()


# In[10]:


import random
dice = []
for i in range(100) :
    dice.append(random.randint(1,6))
print(dice)
plt.hist(dice, bins=6)


# In[12]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding = 'utf8')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))
        
plt.hist(result, bins=100, color = 'skyblue')
plt.show()


# In[3]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding = 'utf8')
data = csv.reader(f)
next(data)
aug = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '':
        if month =='08':
            aug.append(float(row[-1]))
        
plt.hist(aug, bins=100, color = 'skyblue')
plt.show()


# In[6]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', encoding = 'utf8')
data = csv.reader(f)
next(data)
jan = []
aug = []

for row in data :
    month1 = row[0].split('-')[1]
    month2 = row[0].split('-')[1]
    if row[-1] != '':
        if month2 == '01':
            jan.append(float(row[-1]))
        if month1 =='08':
            aug.append(float(row[-1]))
        
plt.hist(aug, bins=100, color = 'skyblue', label = 'Aug')
plt.hist(jan, bins=100, color = 'red', label = 'Jan')
plt.legend()
plt.show()


# In[10]:


import matplotlib.pyplot as plt
import random
import numpy as np
result = []
for i in range(13) :
    result.append(random.randint(1, 1000))
print(sorted(result))


plt.boxplot(result)
plt.show()
result=np.array(result)
print("1/4: "+str(np.percentile(result,25)))
print("2/4: "+str(np.percentile(result,50)))
print("3/4: "+str(np.percentile(result,75)))


# In[12]:


import csv
import numpy as np
import matplotlib.pyplot as plt
f = open('seoul.csv', encoding='utf8')
data = csv.reader(f)
next(data)
result = []
for row in data :
    if row[-1] != '':
        result.append(float(row[-1]))
        
plt.boxplot(result)
plt.show()
result=np.array(result)
print("1/4: "+str(np.percentile(result,25)))
print("2/4: "+str(np.percentile(result,50)))
print("3/4: "+str(np.percentile(result,75)))


# In[24]:


import csv
import numpy as np
import matplotlib.pyplot as plt
f = open('seoul.csv', encoding='utf8')
data = csv.reader(f)
next(data)
jan = []
aug = []

for row in data :
    month1 = row[0].split('-')[1]
    month2 = row[0].split('-')[1]
    if row[-1] != '':
        if month2 == '01':
            jan.append(float(row[-1]))
        if month1 =='08':
            aug.append(float(row[-1]))
        
plt.boxplot(jan)
plt.boxplot(aug)
plt.show()
jan=np.array(jan)
print("1/4: "+str(np.percentile(jan,25)))
print("2/4: "+str(np.percentile(jan,50)))
print("3/4: "+str(np.percentile(jan,75)))
aug=np.array(aug)
print("1/4: "+str(np.percentile(aug,25)))
print("2/4: "+str(np.percentile(aug,50)))
print("3/4: "+str(np.percentile(aug,75)))


# In[27]:


import matplotlib.pyplot as plt
import csv

f=open('seoul.csv', encoding='utf8')
data=csv.reader(f)
next(data)

month=[[], [], [], [], [], [], [], [], [], [], [], []]
for row in data :
    if row[-1] != '' :
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))
          
plt.boxplot(month)
plt.show()


# In[30]:


import matplotlib.pyplot as plt
import csv

f=open('seoul.csv', encoding='utf8')
data=csv.reader(f)
next(data)

day = []
for i in range(31) :
    day.append([])
for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '08' :
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))
 
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.boxplot(day, showfliers=False)
plt.show()


# In[38]:


#1년 중 일교차가 가장 큰달
import matplotlib.pyplot as plt
import csv

f=open('seoul.csv', encoding='utf8')
data=csv.reader(f)
next(data)
month = [[], [], [], [], [], [], [], [], [], [], [], []]
for row in data :
    if row[-1] != '' and row[-2] != '':
        result = float(row[-1])-float(row[-2])
        month[int(row[0].split('-')[1])-1].append(result)
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.boxplot(month, showfliers =False)
plt.show()


# In[ ]:




