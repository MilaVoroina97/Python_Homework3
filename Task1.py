# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
# нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number

from random import randint
from unittest import result

def create_array(size):
    array = []
    buff = 0
    for i in range(size):
        buff = randint(1,100) #check_digit('Введите любое целое положтельное число: ')
        array.append(buff)
    return array


n = check_digit('Введите количество элементов массива: ')
result = create_array(n)
print(result)

def sum_of_odd_index(array):
    sum = 0
    for i in range(len(array)):
        if i % 2 != 0:
            sum += array[i]
            print(f'На нечетных позициях элемент : {array[i]}')
    return sum

print(f'Сумма элементов списка, стоящих на нечётных позициях: {sum_of_odd_index(result)}')




    

