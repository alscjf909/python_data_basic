#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
f=open('subwayfee.csv',encoding='utf8')
data = csv.reader(f)
next(data)
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    print(row)
        


# In[13]:


import csv
f=open('subwayfee.csv',encoding='utf8')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 :
        rate = row[4]/row[6]
        if rate > mx :
            mx = rate
            print(row, round(rate,2))
print(mx)


# In[15]:


import csv
f=open('subwayfee.csv',encoding='utf8')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6])>10000:
        rate = row[4]/(row[6]+row[4])
        if rate > 0.94 :
            mx = rate
            print(row, round(rate,2))
print(mx)


# In[23]:


import csv
f=open('subwayfee.csv',encoding='utf8')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
mx_station = ''
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6])>10000:
        rate = row[4]/(row[6]+row[4])
        if rate > mx :
            mx = rate
            mx_station = row[3]+''+row[1]
            
print(mx_station, round(mx*100,2))


# In[27]:


import csv
import matplotlib.pyplot as plt
f=open('subwayfee.csv',encoding='utf8')
data = csv.reader(f)
next(data)
c=['#14CCC0','#389993','#FF1C6A', '#CC14AF']
label = ['유임승차', '유임하차', '무임승차', '무임하차']
plt.rc('font', family = 'Malgun Gothic')
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3]+''+row[1])
    plt.pie(row[4:8],labels=label,colors=c,autopct='%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3]+''+row[1]+'.png')
    plt.show()


# In[28]:





# In[ ]:




