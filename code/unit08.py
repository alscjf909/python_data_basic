#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm #manage불러오는 것
f = open('age.csv', encoding = 'utf8')
data = csv.reader(f)
result = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요 :')

for row in data :
    if name in row[0] :
        for i in row[3:] :
            result.append(int(i.replace(',','')))
print(result)

plt.style.use('fast')
plt.rcParams['font.family']= 'Malgun Gothic' #요거 있어야 한글나옴
plt.title(name + '인구구조')
plt.plot(result)
plt.show()
#font_list = [font.name for font in fm.fontManager.ttflist]
#font_list


# In[2]:


import csv
import matplotlib.pyplot as plt
f= open('age.csv', encoding = 'utf8')
data = csv.reader(f)

result = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            result.append(int(i.replace(',','')))
print(len(result))
plt.figure(figsize = (10,2))
plt.bar(range(101), result)
plt.show()


# In[3]:


import csv
import matplotlib.pyplot as plt
f= open('age.csv', encoding = 'utf8')
data = csv.reader(f)

result = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            result.append(int(i.replace(',','')))
print(len(result))
plt.figure(figsize = (2,10))
plt.barh(range(101), result)
plt.show()


# In[6]:


import csv
f = open('gender.csv', encoding='utf8')
data=csv.reader(f)
m=[]
f=[]

for row in data :
    if '신도림' in row[0]:
        for i in range(0,101) :
            m.append(int(row[i+3]))
            f.append(int(row[-(i+1)]))
f.reverse()
                     


# In[22]:


import csv
import matplotlib.pyplot as plt
f = open('gender.csv', encoding='utf8')
data=csv.reader(f)
m=[]
f=[]

for row in data :
    if '신도림' in row[0]:
        for i in row[3:104] :
            m.append(int(i))
        for i in row[106:207] :
            f.append(-int(i))
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('신도림 지역의 남녀 성별 인구 분포')
               
plt.barh(range(101),m,label='남성')
plt.barh(range(101),f,label='여성')
plt.show()


# In[29]:


import csv
import matplotlib.pyplot as plt
f = open('gender.csv', encoding='utf8')
data=csv.reader(f)
m=[]
f=[]
name = input('찾고 싶은 지역의 이름을 알려주세요 :')

for row in data :
    if name in row[0]:
        for i in row[3:104] :
            m.append(int(i))
        for i in row[106:207] :
            f.append(-int(i))
plt.rc('font',family='Malgun Gothic')
plt.figure(figsize = (2,5))
plt.rcParams['axes.unicode_minus'] = False

plt.title(name+'지역의 남녀 성별 인구 분포')
               
plt.barh(range(101),m,label='남성')
plt.barh(range(101),f,label='여성')
plt.show()
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[ ]:




