#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
import matplotlib.pyplot as plt
f= open('gender.csv',encoding='utf8')
data = csv.reader(f)
m=[]
f=[]
name = input('궁금한 동네를 입력해주세요')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i].replace(',','')))
            f.append(int(row[i+103].replace(',','')))
        break
plt.plot(m, label='Male')
plt.plot(f, label='Female')
plt.legend()
plt.show()


# In[16]:


import csv
import matplotlib.pyplot as plt
f= open('gender.csv',encoding='utf8')
data = csv.reader(f)
m=[]
f=[]
result = []
name = input('궁금한 동네를 입력해주세요')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i].replace(',','')))
            f.append(int(row[i+103].replace(',','')))
            result.append(int(m[i - 3]) - int(f[i - 3]))
        break
plt.bar(range(101), result) 
# 막대그래프로 그리기
plt.show()


# In[19]:


import matplotlib.pyplot as plt
plt.scatter([1 ,2 ,3 ,4], [10, 30, 20, 40], s=[30,60,90,120], c=['red', 'blue', 'green', 'gold'])
plt.show()


# In[23]:


import matplotlib.pyplot as plt

plt.scatter([1 ,2 ,3 ,4], [10, 30, 20, 40], s=[30,60,90,120], c=range(4), cmap='jet')
# cmap = 스타일, c = 색깔, s = 사이즈
# https://matplotlib.org/tutorials/colors/colormaps.html 다양한 컬래맵 사용 가능
plt.colorbar()
plt.show()


# In[26]:


import matplotlib.pyplot as plt
import random

x=[]
y=[]
size=[]
for i in range(100) :
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))
plt.scatter(x, y, s = size, c= size, cmap = 'jet', alpha = 0.7)
# alpha = 투명도
plt.colorbar()
plt.show()


# In[34]:


import csv
import math
import matplotlib.pyplot as plt
f= open('gender.csv',encoding='utf8')
data = csv.reader(f)
m=[]
f=[]
size = []
name = input('궁금한 동네를 입력해주세요')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i].replace(',','')))
            f.append(int(row[i+103].replace(',','')))
            size.append(math.sqrt(int(m[i-3])+int(f[i-3])))
        break
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.figure(figsize=(10,5), dpi=300)
plt.title(name+'지역의 성별 인구 그래프')
plt.scatter(m, f, s=size, c=range(101), alpha =0.5, cmap='jet')
plt.colorbar()
plt.plot(range(max(m)),range(max(m)),'g')
plt.xlabel('남성 인구수')
plt.ylabel('여성 인구수')
plt.show()


# In[ ]:




