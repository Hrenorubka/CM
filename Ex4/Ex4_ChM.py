#!/usr/bin/env python
# coding: utf-8

# # Задание №4 Вычисление интеграла по формуле Гауса с 3-мя
# Выполнил: Ермолаев Илья 381803-3

# In[1]:


import math


# Зададим исходную функцию

# In[2]:


def inpFunc(x):
    return math.sqrt(1 + 2 * x)


# In[3]:


def ReplacementX(left, right, t):
    return (right + left) / 2.0 + ((right - left) / 2.0) * t 


# Напишем функцию, реализующую вычисление интеграла по формуле Гаусса с 3-мя узлами:

# In[4]:


def threeStepGauss(left, right):
    x1 = - math.sqrt(3.0 / 5.0)
    x2 = 0.0
    x3 = math.sqrt(3.0 / 5.0)
    x1R = ReplacementX(left, right, x1)
    x2R = ReplacementX(left, right, x2)
    x3R = ReplacementX(left, right, x3)
    eIntegral = (5.0 / 9.0) * inpFunc(x1R) + (8.0 / 9.0) * inpFunc(x2R) + (5.0 / 9.0) * inpFunc(x3R)
    return ((right - left) / 2.0) * eIntegral


# Посчитаем интеграл

# In[5]:


left = 0
right = 1
res = threeStepGauss(left, right)
print('Результат интеграрования: ' + str(res))


# Оценим погрешность
# 
# Для этого нам нужно узнать какой максимум у 6-ой производной нашей функции на отрезке интегрирования. Это мы сделаем ручками.

# In[6]:


maxDerivative = 16.0 / (3.0 * 5.0 * 7.0 * 9.0)
maxEps = (maxDerivative * math.pow(math.factorial(3), 4)) / (math.pow(math.factorial(6), 3) * 7.0)
print(maxEps)


# Результат интегрирования нашей функции при помощи Maple 1.398717474235544 ... Странно, что такая оценка у погрешности =(
# Оставлю еще ссылчку которой пользовался, на всякий случай: https://algowiki-project.org/ru/%D0%9A%D0%B2%D0%B0%D0%B4%D1%80%D0%B0%D1%82%D1%83%D1%80%D0%BD%D1%8B%D0%B5_%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B
