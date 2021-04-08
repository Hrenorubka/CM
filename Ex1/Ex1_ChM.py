#!/usr/bin/env python
# coding: utf-8

# # Задание №1 Интерполяциионый полином
# 
# Выполнил: Ермолаев Илья 381803-3

# Зададим начальные условия

# In[2]:


x = [1.0, 1.1, 1.2, 1.3, 1.4];
y = [0.000000, 0.095310, 0.182322, 0.262364, 0.336472];


# Наши входные данные:

# In[3]:


print(x);
print(y);


# Зададим точку, в которой хотим получить результат интерполирования:

# In[4]:


inp_x = 1.23;


# In[5]:


def getPolLagrJ(x, inp_x, power, i_start, j):
    tmp_P = 1.0;
    for i in range(power + 1):
            if (j != i):
                tmp_P *= (inp_x - x[i + i_start]) / (x[j + i_start] - x[i + i_start]);
    return tmp_P;


# In[6]:


def getValPol(x, y, inp_x, power, i_start):
    P_pow_x = 0.0;
    for j in range(power + 1):
        P_pow_x += (y[j + i_start] * getPolLagrJ(x, inp_x, power, i_start, j));
    return P_pow_x;


# Найдем значение функции в заданной точке, с помощью интерполяционного полинома.
# 
# 1-ой степени:

# In[7]:


P_1_x = 0.0;
power = 1;
i_start = 2;
for j in range(power + 1):
    tmp_P = 1.0;
    for i in range(power + 1):
        if (j != i):
            tmp_P *= (inp_x - x[i + i_start]) / (x[j + i_start] - x[i + i_start]);
    P_1_x += (y[j + i_start] * tmp_P);
print("Значение интерполяционного полинома в заданной точке:\n", P_1_x);


# 2-ой степени, взяв узлы с x = 1.1 по x = 1.3:

# In[8]:


P_2_x_1 = 0.0;
power = 2;
i_start = 1;
for j in range(power + 1):
    tmp_P = 1.0;
    for i in range(power + 1):
        if (j != i):
            tmp_P *= (inp_x - x[i + i_start]) / (x[j + i_start] - x[i + i_start]);
    P_2_x_1 += (y[j + i_start] * tmp_P);
print("Значение интерполяционного полинома в заданной точке:\n", P_2_x_1);


# 2-ой степени, взяв узлы с x = 1.2 по x = 1.4:

# In[9]:


P_2_x_2 = 0.0;
power = 2;
i_start = 2;
for j in range(power + 1):
    tmp_P = 1.0;
    for i in range(power + 1):
        if (j != i):
            tmp_P *= (inp_x - x[i + i_start]) / (x[j + i_start] - x[i + i_start]);
    P_2_x_2 += (y[j + i_start] * tmp_P);
print("Значение интерполяционного полинома в заданной точке:\n", P_2_x_2);


# # Итог
# Значение интерполяционного полинома 1-ой степени в заданной точке:

# In[10]:


print(P_1_x);


# Значение интерполяционного полинома 2-ой степени в заданной точке, взяв узлы с x = 1.1 по x = 1.3:

# In[11]:


print(P_2_x_1);


# Значение интерполяционного полинома 2-ой степени в заданной точке, взяв узлы с x = 1.2 по x = 1.4:

# In[12]:


print(P_2_x_2);


# In[ ]:




