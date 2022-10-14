# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from unittest import result


def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число  - {error}")
    return number

n = check_digit('Введите любое целое число: ')

def number_system(m):
    m1 = ""
    while m != 0:
        m1 = str(m%2) +  m1
        m = m //2
    print(m1)

number_system(n)

        