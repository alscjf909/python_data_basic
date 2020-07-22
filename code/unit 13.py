#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0., 5., 0.2)
# np.arange(a, b, c) a값부터 b값 까지 c간격으로 점을 찍음
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.plot(x,y,z) x축=변수 y축=변수2, z특성
plt.show()

# 차이점
x=[]
p2=[]
p3=[]
for i in range(0, 50, 2):
    x.append(i/10)
    p2.append((i/10)**2)
    p3.append((i/10)**3)
plt.plot(t,t, 'r--', t, p2, 'bs', t, p3, 'g^')
plt.show()


# In[4]:


import numpy as np
print(np.pi)
print(np.sin(0))
print(np.cos(np.pi))


# In[5]:


import numpy as np
a = np.random.rand(5)
#rand => 0~1사이의 값 무작위로
print(a)
print(type(a))


# In[7]:


import numpy as np
print(np.random.choice(6,10))


# In[8]:


import numpy as np
print(np.random.choice(10,6, replace=False))


# In[11]:


import numpy as np
print(np.random.choice(6,10, p=[0.1,0.2,0.3,0.2,0.1,0.1]))


# In[13]:


import matplotlib.pyplot as plt
import numpy as np
dice = np.random.choice(6,1000000, p=[0.1,0.2,0.3,0.2,0.1,0.1])

plt.hist(dice,bins=6)
plt.show()


# In[14]:


import matplotlib.pyplot as plt
import numpy as np

x= np.random.randint(10, 100, 200)
# randint(a, b, c) a~b까지 200가지
y= np.random.randint(10, 100, 200)
size = np.random.rand(100)*100

plt.scatter(x,y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()
# https://docs.scipy.org/doc/numpy-1.13.0/reference/


# In[22]:


import numpy as np
a = np.array([1,2,3,4])
print(a)
print(a[1],a[-1])
print(a[1:])


b= np.array([1,2,'3',4])
# numpy array는 한가지 타입의 데이터만을 저장할 수 있습니다.
print(b)

# zeros(n) 크기가 n이고 요소 값이 0인 행렬 생성
c= np.zeros(10)
print(c)


# ones(n) 크기가 n이고 요소 값이 1인 행렬 생성
d=np.ones(10)
print(d)

#eye(n)  n*n 단위 배열 생성
e=np.eye(3)
print(e)


# arange(n) 0부터 n-1까지의 배열 생성 interval 1
# arange(n,k) n부터 k-1까지의 배열 생성 interval 1
# arange(n,k,p) n부터 k-1까지의 배열 생성 interval p
print(np.arange(3))
print(np.arange(3,7))
print(np.arange(3,7,2))

f=np.arange(1,2,0.1)
# linspace(a, b, c) a부터 b까지를 c개로 나눔
g=np.linspace(1,2,11)

h = np.arange(-np.pi, np.pi, np.pi/10)
i = np.linspace(-np.pi, np.pi, 20)
print(h)
print(i)


# In[24]:


import numpy as np

# 행렬 + n 은 각 요소에 n씩 더해진다.
a = np.zeros(10) + 5
print(a) 
# 행렬 함수은 각 요소에 함수가 계산된다.
b= np.linspace(1,2,11)
print(np.sqrt(b))


# In[26]:


import numpy as np
import matplotlib.pyplot as plt
a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.show()


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
a=np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.plot(a, np.cos(a))
plt.plot(a+np.pi/2, np.sin(a))
plt.show()


# In[7]:


import numpy as np
a=np.arange(-5,5)
print(a)
print(a<0)
print(a[a<0])
mask1 = abs(a)>3  # True인 값만 보내줌
print(a[mask1])
mask2=abs(a)%2==0
print(a[mask1+mask2])   # 둘 중 하나의 조건이라도 참일 경우
print(a[mask1*mask2])   # 두가지 조건이 모두 참일 경우


# In[1]:


import numpy as np
import matplotlib.pyplot as plt
x=np.random.randint(-100, 100, 1000)# 1000개의 랜덤 값 추출
y=np.random.randint(-100, 100, 1000)
size = np.random.rand(100) * 100
mask1 = abs(x) > 50
mask2 = abs(y) > 50
x= x[mask1+mask2]
y= y[mask1+mask2]
plt.scatter(x, y, s=size, c=x, cmap = 'jet', alpha =0.7)
plt.colorbar()
plt.show()


# In[ ]:




