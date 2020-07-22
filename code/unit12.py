#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
f=open('subwaytime.csv', encoding='utf8')
data =csv.reader(f)
next(data)
next(data)
for row in data :
    row[4:]=map(int,row[4:])
    #map함수 리스트를 변경하기 쉬움 map(function, 불러올 데이타)
    print(row)


# In[6]:


import csv
import matplotlib.pyplot as plt
f=open('subwaytime.csv', encoding='utf8')
data =csv.reader(f)
next(data)
next(data)
result = []
for row in data :
    row[4:]=map(int,row[4:])
    result.append(row[10])
print(len(result))
print(result)
plt.style.use('ggplot')
plt.figure(figsize = (5,2))
plt.bar(range(len(result)),result)
plt.show()


# In[11]:


import csv
import matplotlib.pyplot as plt
f=open('subwaytime.csv', encoding='utf8')
data =csv.reader(f)
next(data)
next(data)
result = []
for row in data :
    row[4:]=map(int,row[4:])
    result.append(sum(row[10:15:2]))
result.sort()
print(len(result))
print(result)
plt.style.use('ggplot')
plt.figure(figsize = (5,5))
plt.bar(range(len(result)),result)
plt.show()


# In[20]:


import csv
import matplotlib.pyplot as plt
f=open('subwaytime.csv', encoding='utf8')
data =csv.reader(f)
next(data)
next(data)
result = []
mx = 0;
mx_station = ''
for row in data :
    row[4:]=map(int,row[4:])
    result.append(sum(row[10:15:2]))
    if sum(row[10:15:2])> mx :
        mx = sum(row[10:15:2])
        mx_station = row[3]+'('+row[1]+')'
result.sort()
print(mx_station,mx)


# In[32]:


import csv
import matplotlib.pyplot as plt
f=open('subwaytime.csv', encoding='utf8')
data =csv.reader(f)
next(data)
next(data)
mx = [0] * 24
mx_station = [''] * 24
for row in data : 
    row[4:] = map(int, row[4:])
    for j in range(24):
        a=row[j*2+4]
        if a> mx[j] :
            mx[j] = a
            mx_station[j] = row[3]+'('+str(j+4)+'시)'
print(mx_station)
print(mx)
plt.rc('font', family='Malgun Gothic')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation=90)
# xticks x축 변수 rotation 글자 회전
plt.show()


# In[37]:


import csv
import matplotlib.pyplot as plt
f=open('subwaytime.csv', encoding='utf8')
data =csv.reader(f)
next(data)
next(data)
s_in = [0]*24
s_out = [0]*24
for row in data : 
    row[4:] = map(int, row[4:])
    for j in range(24):
        s_in[j] += row[j*2+4]
        s_out[j] += row[j*2+5]
print(mx_station)
print(mx)
plt.rc('font', family='Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(s_in, label='승차')
plt.plot(s_out, label='하차')
plt.legend(loc=3)
plt.xticks(range(24), range(4,28))
# xticks x축 변수 rotation 글자 회전

plt.show()


# In[ ]:




