#!/usr/bin/env python
# coding: utf-8

# In[22]:


x=list(input().split(" "))
del x[-5:]
print(tuple(x))


# In[32]:


x=input().split(" ")
y=input().split(" ")
z={x:y}
print(z)


# In[10]:


price=int(input())
cash=input()
if cash=="Cash3000":
    price=price-3000
    print(price)
if cash=="Cash5000":
    price=price-5000
    print(price)


# In[15]:


a,b,c,d=map(int, input().split(" "))
score=(a+b+c+d)/4
if a>100 or b>100 or c>100 or d>100 :
    print("잘못된 입력입니다.")
    if score>=80:
        print("합격")
    else:
        print("불합격")


# In[17]:


age=int(input())
balance=9000
if 7 <= age <=12:
    balance=balance-650
    print(balance)
elif 13 <= age <=18:
    balance=balance-1050
    print(balance)
else:
    balance=balance-1250
    print(balance)
    


# In[19]:


num=int(input())
for i in range(1,10):
    print(num,"*",i, "=",num*i)


# In[ ]:


money=int(input())
while money>1350:
    money=money-1350
    print(money)


# In[2]:


start, stop = map(int, input().split(" "))
while True:
    for i in range(start, stop+1):
        if i%10==3:
            continue
        print(i, end=" ")
    if i==stop:
            break


# In[17]:


h=int(input())
for i in range(1,h*2,2):
    a="*"*i
    print("{0:^10}".format(a))


# In[7]:


a, b=map(int,input().split(" "))
c=[]
for i in range(a,b+1):
    c.append(2**i)
print(c)


# In[ ]:


#지뢰찾기


# In[22]:


a=input().split()
count=0
for i in a:
    if i.strip(",.")=="the":
        count+=1
print(count)


# In[35]:


a=input().split(";")
a = list(map(int, a))
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i])


# In[37]:


keys = input().split()
values = map(int, input().split())
x = dict(zip(keys, values))
del x["delta"]
print(x)


# In[38]:


a, b =map(int, input().split())
a={i for i in range(1, a+1) if a%i==0}
b={i for i in range(1, a+1) if b%i==0}
divisor = a & b
result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)


# In[39]:



with open('words.txt','r') as file:
    text=file=readline()
    words=text.split()
    for word in words:
        if 'c' in word:
            print(word.sprit(",."))


# In[ ]:


#n_gram


# In[3]:


x, y = map(int, input().split())
def calc(x,y):
    return x+y,x-y,x*y,x/y
a,s,m,d=calc(x,y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))


# In[ ]:




