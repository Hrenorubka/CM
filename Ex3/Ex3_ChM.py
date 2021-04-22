#!/usr/bin/env python
# coding: utf-8

# # Задание №3 Вычисление интеграла по формуле Симпсона
# Выполнил: Ермолаев Илья 381803-3

# In[1]:


import math


# Заранее напишем функцию, реализующую формулу Симпсона:

# In[2]:


def SimpsonFormule(xiLeft, xiRight, fiLeft, fiRight, fiCenter):
    hi = (xiRight - xiLeft) / 2.0
    return (hi / 3.0) * (fiLeft + 4.0 * fiCenter + fiRight)


# Зададим начальные условия:

# In[3]:


def inpFunc(x):
    return(1.0 / (x + math.cos(x)))

inpEps = 3.0 * 0.0001
left = 0.0
right = math.pi


# Зададим начальный шаг:

# In[4]:


n = 1 # начальное число разбиений
h = (right - left) / n # начальный шаг


# Построим сетку при заданном шаге:

# In[5]:


reachedEps = 1.000 # достигнутая погрешность
while (reachedEps > inpEps):
    n = n * 10
    h = (right - left) / n
    x = [left]
    y = [inpFunc(left)]
    tmp = left
    for i in range(0, n):
        tmp = tmp + h / 2.0
        x.append(tmp)
        y.append(inpFunc(tmp))
        tmp = tmp + h / 2.0
        x.append(tmp)
        y.append(inpFunc(tmp))
    funci = []
    for i in range(0, n):
        funci.append(SimpsonFormule(x[2 * i], x[2 * i + 2], y[2 * i], y[2 * i + 1], y[2 * i + 2]))
    h = (right - left) / (2 * n)
    x2 = [left]
    y2 = [inpFunc(left)]
    tmp = left
    for i in range(0, 2 * n):
        tmp = tmp + h / 2.0
        x2.append(tmp)
        y2.append(inpFunc(tmp))
        tmp = tmp + h / 2.0
        x2.append(tmp)
        y2.append(inpFunc(tmp))
    funci2 = []
    for i in range(0, 2 * n):
        funci2.append(SimpsonFormule(x2[2 * i], x2[2 * i + 2], y2[2 * i], y2[2 * i + 1], y2[2 * i + 2]))
    reachedEps = abs(funci[0] - funci2[0])
    for i in range(1, n):
        curEps = abs(funci[i] - funci2[i * 2]) 
        if (reachedEps < curEps):
            reachedEps = curEps
resFunc = 0.0 # Результат интегрирования
for i in range(len(funci)):
    resFunc = resFunc + funci[i]
print("Полученный интеграл: " + str(resFunc))


# In[ ]:




