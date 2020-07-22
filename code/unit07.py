#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm #manage불러오는 것
f = open('age.csv', encoding = 'utf8')
data = csv.reader(f)
result = []


for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            result.append(int(i))
print(result)



# In[21]:


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


# In[24]:


import matplotlib.pyplot as plt
plt.bar([0, 1, 2, 4, 6, 10], [1, 2, 3, 5, 6, 7])
plt.bar([0, 3, 2, 1, 6, 10], [1, 2, 3, 5, 6, 7])
plt.show()


# In[32]:


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


# In[34]:


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


# In[ ]:




