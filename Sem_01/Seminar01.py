
import msvcrt
import os


def task01():
    """ Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели."""
    nameDaysWeek = [
        '0', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    print()
    numberDay = int(input('Введите номер дня недели :'))
    if numberDay > 0 and numberDay <= 7:
        print(
            f' {numberDay} день недели называется: "{nameDaysWeek[numberDay]}"')
    else:
        print(f'День недели {numberDay} не существует!')


def task02():
    """
    Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
    """

    print('\nВведите координаты двух точек.')
    print('(десятичный разделитель - точка!)')
    dotA = (float(input('координата X точки A: ')),
            float(input('координата Y точки A: ')))
    dotB = (float(input('координата X точки B: ')),
            float(input('координата Y точки B: ')))

    distAB = ((dotA[0]-dotB[0])**2+(dotA[1]-dotB[1])**2)**0.5

    print(f"расстояние между точками: {round(distAB, 3)}")


def task03():
    """ Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). Пример:
    \n1 -> x > 0, y > 0 """

    coordQuartRanges = ('', 'X > 0, Y > 0', 'X < 0, Y > 0',
                        'X < 0, Y < 0', 'X > 0, Y < 0')
    coordQuartNumbers = ('', 'I', 'II', 'III', 'IV')
    print()
    inputCheck = False
    while inputCheck == False:
        userInput = int(input('Введите номер координатной четверти (1 - 4):'))
        if userInput >= 1 and userInput <= 4:
            inputCheck = True

    print(f'{coordQuartNumbers[userInput]} -> {coordQuartRanges[userInput]}')


def task04():
    """Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N. Пример:
    \n5 -> 2, 4
    \n8 -> 2, 4, 6, 8"""

    print('\nВывод четных чисел от 1 до N')
    userInput = int(input('Введите число N : '))
    stop = userInput+1
    print(f'{userInput} ', end='-> ')
    for a in range(1, stop):
        if a % 2 == 0:
            if a == userInput or a == userInput-1:
                strEnd = ''
            else:
                strEnd = ', '
            print(a, end=strEnd)


check = True
while check:
    os.system('clear')
    numTask = int(input('Номер задачи 1-4 :'))
    if numTask >= 1 and numTask <= 4:
        match numTask:
            case 1:
                task01()
            case 2:
                task02()
            case 3:
                task03()
            case 4:
                task04()

    print('\n\nЗавершить - клавиша enter, \nпродолжить - любая')
    c = bytes(msvcrt.getch())
    if c == b'\r':
        check = False
