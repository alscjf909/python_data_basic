#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
            m.append(int(i.replace(',','')))
        for i in row[106:] :
            f.append(-int(i.replace(',','')))
        break
plt.rc('font',family='Malgun Gothic')
plt.figure(figsize = (2,5))
plt.rcParams['axes.unicode_minus'] = False

plt.title(name+'지역의 남녀 성별 인구 분포')
               
plt.barh(range(101),m,label='남성')
plt.barh(range(101),f,label='여성')
plt.show()


# In[13]:


import csv
import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic') # 없으면 한글 깨짐
size = [2441, 2312, 1031, 1233]
label = ['A형', 'B형', 'AB형', 'O형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
plt.axis('equal')
plt.pie(size, labels =label, autopct='%.1f%%', colors=color, explode=(0, 0, 0.1, 0))
#.pie => 원형 그래프
# labels => 라벨링 하기
# autopct(auto percent) => 각각의 속성값 적기 %.1f%% 소수점 아래 둘째 자리에서 반올림한 값을 표시하자
# 리스트 마다 겹친다
# 돌출 비율 explode로 설정할 수 있게 0이 돌출되지 않음을 의미한다.
plt.legend()
plt.show()


# In[17]:


import csv
import matplotlib.pyplot as plt
f = open('gender.csv', encoding='utf8')
data=csv.reader(f)

size=[]
name = input('찾고 싶은 지역의 이름을 알려주세요 :')

for row in data :
    if name in row[0] :
        m=0
        f=0
        for i in range(101) :
            m+= int(row[i+3].replace(',',''))
            f+= int(row[i+106].replace(',',''))
        break

size.append(m)
size.append(f)
print(size)
plt.rc('font', family = 'Malgun Gothic') # 없으면 한글 깨짐
color = ['crimson','darkcyan']
plt.axis('equal')
plt.pie(size, labels=['남','여'], autopct='%.1f%%',colors=color, startangle=90)
# startangle 파이 차트의 시작 각도를 정해준다. 90으로 설정하면 처음 시작이 3시 방향이므로 12시 정각 위치에서 그래프가 시작된다.
plt.title(name+'지역의 남녀 성별 비율')
plt.show()


# In[ ]:





# In[ ]:




