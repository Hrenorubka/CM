#!/usr/bin/env python
# coding: utf-8

# # Задание №2. Вычисление производной.
# 
# Выполнил: Ермолаев Илья 381803-3

# In[1]:


import decimal;
import math;


# In[2]:


def CreateFiniteDifferences(diff_y, order):
    if (order <= 0):
        return diff_y;
    out = [];
    for i in range(len(diff_y) - 1):
        out.append(diff_y[i + 1] - diff_y[i]);
    return CreateFiniteDifferences(out, order - 1);


# Зададим начальный шаг, его изменение и точку в которой хотим посчитать производную:

# In[3]:


start_h = 0.1;
end_h = 0.01;
delta_h = 0.01;
inp_x = 1.15;
i_h = start_h;
value_derivative = [];
while i_h >= end_h:
    i_h_printable = decimal.Decimal(i_h).normalize();
    print("Текущий шаг: " + str(i_h_printable));
    point_x = [inp_x - i_h, inp_x, inp_x + i_h]; 
    point_y = [];
    decimal.getcontext().prec = 5;
    # Найдем 3 значения функции для нашего шага, в точках f(inp_x - h), f(inp_x), f(inp_x + h)
    for i in range(0, 3):
        print('Значения узлов point_x[i] для данного шага: ' + str(decimal.Decimal(point_x[i]).normalize()));
        point_y.append(decimal.Decimal(point_x[i]).exp());
    # Найденные значения функции в точках:
    for i in point_y:
        print('Значения point_y[i] в узлах x_point[i]: ' + str(i));
    derivative = (point_y[2] - point_y[0]) / decimal.Decimal(2.0 * i_h);
    value_derivative.append(derivative);
    print('Значение производной = '+ str(derivative) + ' при h = ' + str(i_h_printable.normalize()));
    i_h = i_h - delta_h;


# Итоговые значения:

# In[4]:


i_h = start_h;
for i in range(10):
    i_h_printable = decimal.Decimal(i_h).normalize();
    abs_eps = value_derivative[i];
    print('Шаг: ' + str(i_h_printable) + '    Значение производной: ' + str(abs_eps) + '\n');
    i_h = i_h - delta_h;

print(decimal.Decimal(inp_x).exp().normalize());
# Посмотрим на абсолютную погрешность при каждом шаге:

# In[5]:


i_h = start_h;
for i in range(10):
    i_h_printable = decimal.Decimal(i_h).normalize();
    abs_eps = (decimal.Decimal(inp_x).exp() - value_derivative[i]).copy_abs();
    print('Шаг: ' + str(i_h_printable) + '    Абс. погрешность: ' + str(abs_eps) + '\n');
    i_h = i_h - delta_h;


# Найдем оптимальный шаг численного дифференцироварния.

# Чтобы оценить погрешность оператора, ручками найдем производную 3-его(?) порядка, и найдем ее максимум. Он достигается в точке x = 1.25

# In[6]:


changeable_const = decimal.Decimal(1.25).exp();
print('Максимум 3-ей производной: ' + str(changeable_const));
operation_delta = (changeable_const * decimal.Decimal(0.01) ) / decimal.Decimal(6.0);
print('Погрешность оператора: ' + str(operation_delta));


# Определим вычислительную погрешность  

# In[7]:


variables_delta = decimal.Decimal(0.00005) / decimal.Decimal(0.1);
print('Вычислительная погрешность  ' + str(variables_delta));


# Определим оптимальный шаг:

# In[8]:


optimal_h = ((decimal.Decimal(3.0) * decimal.Decimal(0.00005)) / (changeable_const)) ** (decimal.Decimal(1.0) / decimal.Decimal(3.0));
print('Оптимальный шаг: ' + str(optimal_h));


# # Итог:

# ### Изменение абсолюной погрешности на заданнной сетке при изменении шага сетки:

# In[9]:


i_h = start_h;
for i in range(10):
    i_h_printable = decimal.Decimal(i_h).normalize();
    abs_eps = (decimal.Decimal(inp_x).exp() - value_derivative[i]).copy_abs();
    print('Шаг: ' + str(i_h_printable) + '    Абс. погрешность: ' + str(abs_eps) + '\n');
    i_h = i_h - delta_h;


# ### Оценка общей погрешности при шаге 0.1:

# In[10]:


print(operation_delta + variables_delta);


# ### Оптимальный шаг:

# In[11]:


print(optimal_h);


# In[ ]:




