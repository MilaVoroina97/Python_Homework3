# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , причем чтоб количество
#  элементов было четное. Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива, причем чтобы 
#  каждый гарантированно переместился на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре,
#  то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

from random import randint

def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number

def create_array(size,size2):
    array = []
    for i in range(size):
        buff = []
        for j in range(size2):
            value = randint(1,100)
            buff.append(value)
        array.append(buff)
    return array


def printMatrix (matrix): 
   for i in range (len(matrix) ): 
      for j in range ( len(matrix[i]) ): 
          print ( "{:4d}".format(matrix[i][j]), end = "" ) 
      print ()

def peremesh(matrix,size1,size2):
    temp = 0
    new_i = 0
    new_j = 0
    for i in range(size1):
        for j in range(size2):
            new_i = randint(0,size1-2)
            new_j = randint(0,size2-2)
            temp = matrix[i][j]
            matrix[i][j] = matrix[new_i][new_j]
            matrix[new_i][new_j] = temp
    return matrix


m = check_digit('Введите количество строк массива: ')
n = check_digit('Введите количество столбцов массива: ')
if (m * n) % 2 == 0:
    matrix = create_array(m,n)
    printMatrix(matrix)
    peremesh(matrix,m,n)
    print('Перемешанный массив: ')
    printMatrix(matrix)
else:
    print('Введите размерность массива так, чтобы там было четное количество элементов.')


