# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def check_digit(text):
    check = False
    while not check:
        try:
            number = float(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите ЦЕЛОЕ или ДРОБНОЕ число  - {error}")
    return number

def create_array(n):
    array = []
    for i in range(n):
        array.append(check_digit('Введите целое или дробное число через точку (.): '))
    return array


def dif_of_fraction(array):
    array1 = []
    for i in array:
        if i % 1 !=0:
            array1.append(round(i%1,4))
    max = array1[0]
    min = array1[0]
    dif = 0
    for j in range(len(array1)):
        if array1[j] > max:
            max = array1[j]
        elif array1[j] < min:
            min = array1[j]
    dif = max - min
    return dif    

try:

    n = int(input('Введите количество элементов массива: '))
    massiv = create_array(n)
    print(f'Разница между максимальным и минимальным значением дробной части элементов: {dif_of_fraction(massiv)}')

except:
    print('Размерность массива должна задаваться именно ЦЕЛЫМ числом. ')



     




