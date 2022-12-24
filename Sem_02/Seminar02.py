import os


def task01():
    '''Задача 1. Напишите программу, которая принимает на вход число N 
    \nи выдает список факториалов для чисел от 1 до N. 
    \nпусть N = 4 -> [1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)'''

    numInput = int(input('Введите целое и положительное число :'))
    factList = []
    for i in range(1, numInput+1):
        factorial = 1
        for j in range(1, i+1):
            factorial = factorial * j
        factList.append(factorial)
    print(f'N = {numInput} -> {factList}')


def task02():
    '''Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.'''

    print('│ x │ y │ z │¬(X ∧ Y) ∨ Z')
    print('-----------------')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f'│ {x} │ {y} │ {z} │ {int(not(x and y) or z)} │')


def task03():
    ''' 
    Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки 
    встречается во второй «one» «onetwonine» - o – 2, n – 3, e – 2'''

    baseStr = 'one'
    strOne = list(set(baseStr))
    strTwo = 'onetwonine'

    result = []
    for i in range(len(strOne)):
        count = 0
        for j in range(len(strTwo)):
            if strOne[i] == strTwo[j]:
                count += 1
        result.append(f' {strOne[i]} - {count} ')
    print(
        f'Символы из строки "{baseStr}" в строке "{strTwo}" встречаются:\n {result}')


def task04():
    """ Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.3 -> [2, 3, -3, -2, -1, 0, 1]  """

    rangBond = int(input('Задайте число для диапазона [-N,N] ->:'))
    sourceList = []
    resultList = []

    for i in range(-rangBond, rangBond+1):
        sourceList.append(i)
    print(f'Список элементов от -{rangBond} до {rangBond} \n{sourceList}')
    userInput = int(input('На сколько элементов сдвинуть вправо? :'))
    charToShift = userInput

    while charToShift > len(sourceList):
        charToShift -= len(sourceList)

    resultList.extend(sourceList[-charToShift:])
    resultList.extend(sourceList[:-len(resultList)])

    print(f'Список сдвинут на {userInput} поз. вправо:\n {resultList}')


os.system('clear')

# task01()
# task02()
# task03()
# task04()
