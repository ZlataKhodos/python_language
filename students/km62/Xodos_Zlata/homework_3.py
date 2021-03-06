#task1--------------------------------------------------------------------------------
"""Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено. """

#defaults
factorial=1

#input
number=int(input("Please, enter a number to calculate factorial")) #натуральне число

#validation
if number<=0:
	print("Input error")

#main
for i in range(1,number+1):
    factorial*=i

#output
print("Factorial of number is: ",factorial)
#-------------------------------------------------------------------------------------

#task2--------------------------------------------------------------------------------
"""По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл. 
Пользоваться математической библиотекой math в этой задаче запрещено.

 """

#defaults
factorial=1
sum=0

#input
high_number=int(input("Enter a high number to calculate sum of factorials")) #натуральне число

#validation
if high_number<=0:
	print("Input error")

#main
for i in range (1,high_number+1):
    factorial*=i
    sum+=factorial

#output
print("Sum of factorials is: ",sum)
#-------------------------------------------------------------------------------------

#task3--------------------------------------------------------------------------------
"""Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. 
Подсчитайте количество нулей среди введенных чисел и выведите это количество. 
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр. """

#defaults
counter=0 #рахує числа-нулі

#input
amount_of_numbers=int(input("How many numbers do you want to use?")) #ціле число елементів, які бажає обробити користувач

#validation
if amount_of_numbers<=0: 
	print("Input error")

#main(and input inside)
for i in range(amount_of_numbers):
    number=int(input("Input a number")) #введення номерів на опрацювання
    if number==0:
        counter+=1 #збільшує лічильник на 1 при виявленні числа, яке дорівнює нулю

#output
print("Amount of zeroes: ",counter)
#-------------------------------------------------------------------------------------

#task4--------------------------------------------------------------------------------
"""По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов. """

#input
high_number=int(input("Enter the last number for stairs")) #скільки максимально цифр містить нижня сходинка

#validation
if high_number>9:
	print("This is not number, this is a numeral") #драбинка може будуватись лише з цифр

#main(and output inside)
for i in range (high_number):
    for j in range(1,i+2):
        print(j,sep="",end="")
    print()
#-------------------------------------------------------------------------------------


#task5--------------------------------------------------------------------------------
"""Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. 
Найдите ее, зная номера оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). 
Программа должна вывести номер потерянной карточки.

Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя. """

#defaults
sum_left_cards=0 #сума номерів не втрачених карток

#input
high_number=int(input("How many cards should exist?")) #натуральне число

#main(and input inside)
sum_all_cards=high_number*(high_number+1)//2 #сума номерів на всіх картках
for i in range (1,high_number):
    card=int(input("Enter a number of card")) #користувач вводить номера карток, що в нього є
    sum_left_cards+=card #сума присутніх карток

#output
print(sum_all_cards-sum_left_cards) #від суми номерів на всіх картках, що мають бути віднімає суму номерів карток, що має користувач
