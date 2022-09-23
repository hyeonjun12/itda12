#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0, 6, 0.1)
y1=np.sin(x)
y2=np.cos(x)

plt.plot(x, y1, label="sin")#x값, y값, 그래프 종류
plt.plot(x, y2, linestyle="--", label="cos")#linestyle=점선, 실선
plt.xlabel("x")#x선
plt.ylabel("y")#y선
plt.title("sin & cos")#그래프 이름
plt.legend()
plt.show()


# In[15]:


import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0, 6, 0.1)
y=np.sin(x)

plt.plot(x,y)
plt.show()


# In[7]:


import numpy as np
x=np.array([[1, 2], [3,4]])
y=np.array([[2.0,3.0],[4.0,5.0]])
print(x+y)


# In[13]:


X=np.array([[51,55],[14,19],[0,4]])# 3X2 2차원 배열
X[0][1]
X>15


# In[14]:


from matplotlib.image import imread
img=imread("cactus.png")#사진 이름 적는 곳
plt.imshow(img)
plt.show()

