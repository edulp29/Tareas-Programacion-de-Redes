#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("Bienvenido a la Calculadora de Python")
print("Seleccione operacion a realizar")
print("1-Suma")
print("2-Resta")
print("3-Multiplicacion")
print("4-Division")
print("5-Exponencial")
x=input("Introduzca el Numero de la operación")
y=float(x)
if y==1:
    a=input("Introduzca primer sumando:")
    b=input("Introduzca segundo sumando:")
    s1=float(a)
    s2=float(b)
    resultado=s1+s2
    print("El resultado de la suma es:", resultado)
elif y==2:
    a=input("Introduzca primer sustraendo:")
    b=input("Introduzca segundo sustraendo:")
    s1=float(a)
    s2=float(b)
    resultado=s1-s2
    print("El resultado de la resta es:", resultado)
elif y==3:
    a=input("Introduzca el multiplicando:")
    b=input("Introduzca el multiplicador:")
    s1=float(a)
    s2=float(b)
    resultado=s1*s2
    print("El resultado de la multiplicacion es:", resultado)
elif y==4:
    a=input("Introduzca el dividendo:")
    b=input("Introduzca el divisor:")
    s1=float(a)
    s2=float(b)
    resultado=s1/s2
    print("El resultado de la division es:", resultado)
elif y==5:
    a=input("Introduzca numero base:")
    b=input("Introduzca el exponente:")
    s1=float(a)
    s2=float(b)
    resultado=s1**s2
    print("El resultado de la division es:", resultado)
else:
    print("Introduzca un numero entre 1 y 5")













