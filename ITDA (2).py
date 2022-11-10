#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def AND(x1, x2,1):
    w1,w2,b=#가중치
    h(x)=x1*w1+x2*w2+b#활성화함수
h(x)=0if(x=<0)
     1if(x>0)
h(a)=a1*w1+a2*w2+b#y의 값을 출력하는 활성화함수(a를 넣었을때)
#가중치 신호를 조합한 결과가 a라는 노드가 되고 활성화 함수 h()통과하여 y라는 노드로 변환된다.
#이 과정이  h()라는 큰 노드안에서 실행되는 과정입니다.


# In[1]:


#활성화 함수는 a를 넣어서 y라는 결과값을 출력하는데 이 y가 0과1 의 출력으로 나뉘기 때문에 계단함수로도 말할 수 있습니다.
#시그모이드함수
def h(x):
    y=1/1+exp(-x)
    print(y)
#exp(-x)=e**-x(e=자연상수)


# In[8]:


import numpy as np
#계단함수
def step_function(x):
    if x>0:
        return 1
    else:
        return 0

def step_function2(x):
    y=x>0
    return y.astype(np.int)#np.int는 넘파이의 실수값을 0을 기준으로 0을 넘으면 1로, 넘지 않으면 0으로 반환해준다.
step_function2(np.array([-1.0,1.0,2.0]))


# In[9]:


def step_function3(x):
    y=x>0
    return y
step_function3(np.array([-1.0,1.0,2.0]))


# In[11]:


import matplotlib.pylab as plt
def step_function(x):
    return np.array(x>0,dtype=np.int)
x=np.arange(-5.0,5.0,0.1)#x축을 -5.0부터 5.0까지 생성
y=step_function(x)#y축을 넘파이 배열의 원소를 인수로 계단 함수를 실행해 결과를 다시 배열로 돌려줌
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()


# In[12]:


#시그모이드 함수
def sigmoid(x):
    return 1/(1+np.exp(-x))
x=np.array([-1.0,1.0,2.0])
sigmoid(x)


# In[15]:


t=np.array([1.0,2.0,3.0])
1.0+t
1 .0/t
#브로드캐스트(1.5.5)기능으로 인하여 위의 식이 계산 가능


# In[17]:


x=np.arange(-5.0,5.0,0.1)
y=sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()


# In[ ]:


def relu(x):
    return np.maximum(0,x)


# In[4]:


import numpy as np
A=np.array([1,2,3,4])
print(A)
np.ndim(A)#배열의 차원수 확인
A.shape#배열의 형상 확인-튜플로 반환
A.shape[0]


# In[5]:


B=np.array([[1,2],[3,4],[5,6]])
print(B)
np.ndim(B)
B.shape


# In[2]:


import numpy as np
A=np.array([[1,2,3],[4,5,6]])
B=np.array([[1,2],[3,4],[5,6]])
np.dot(A,B)
#행렬 A의 1번째 차원의 원소수(열 수)와 행렬 B의 0번쨰 차원의 원소 수(행 수)가 같아야 함


# In[6]:


x=np.array([1,2])
w=np.array([[1,3,5],[2,4,6]])
y=np.dot(x,w)#다차원 배열의 스칼라값을 곱해줌(np.dot)
print(y)

