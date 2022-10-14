# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

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

def create_array(size):
    array = []
    buff = 0
    for i in range(size):
        buff = check_digit('Введите любое целое положтельное число: ')
        array.append(buff)
    return array


n = check_digit('Введите количество элементов массива: ')
result = create_array(n)
print(result)

def prod_of_elements(array):
    prod = 0
    array2 = []
    size = len(array)
    for i in range(len(array)):
        while i < len(array)/2 and size > len(array)/2:
            size -=  1
            prod = array[i] * array[size]
            array2.append(prod)
            i += 1
    return array2

result2 = prod_of_elements(result)
print(f'Произведение пар чисел списка: {result2}')

