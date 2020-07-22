#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
max_temp = -999
max_date = ''
f = open('seoul.csv', encoding = 'utf8')
data = csv.reader(f)
header = next(data)
for row in data :
    if row[-1] == '':
        row[-1] = -999
    row[-1] =float(row[-1])
    print(row)
    if row[-1] > max_temp : 
        max_temp=row[-1]
        max_date =row[0]
f.close()
print('기상 관측 이래 가장 기온이 높았던 날은', max_date+'로', max_temp,'도 였습니다')


# In[ ]:





# In[ ]:





# In[ ]:




