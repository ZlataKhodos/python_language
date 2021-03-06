#task1------------------------------------------------------------
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
"""

from math import sqrt,pow


#input
x1=float(input("Enter coordinate x1"))

y1=float(input("Enter coordinate y1"))

x2=float(input("Enter coordinate x2"))

y2=float(input("Enter coordinate x2"))


#main
def distance(x1,y1,x2,y2):

    length=sqrt(pow(x2-x1,2)+pow(y2-y1,2))

    return length


#output
print(distance(x1,y1,x2,y2))

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
"""

#import
from math import fabs,ceil


#input
number=float(input("Enter a positive number"))

power_num=int(input("Enter an integer n"))



#main
def power(number,power_num):

    result=1

    counter=0

    for counter in range (ceil(fabs(power_num))):

        result*=number

    if power_num<0:

        result=1/result

    return result


#output
print(power(number,power_num))

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.

Решение оформите в виде функции power(a, n).
"""

#main
def power(a, n):

    if n==0:

        return 1

    else:

        return a*power(a,n-1)


#input and output
print(power(float(input("Enter a number")), float(input("Enter a power"))))
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n 
возвращает n-e число Фибоначчи. В этой задаче нельзя использовать 
циклы — используйте рекурсию.
"""

#main
def fib(n):

    if n==1:

        return 1

    elif n==0:

        return 0

    else:

        return fib(n-1)+fib(n-2)



#input
n=int(input("Enter a positive integer number"))


#output
print("This number has a ",fib(n))

#-----------------------------------------------------------------