import os
from math import pi
import re
# os.system('clear')
clscr = os.system('clear')


def start_task():
    decription = [
        '1. Список простых множителей числа',
        '2. Найти закончившееся мороженое',
        '3. Задать точность числа π'
    ]
    for _ in decription:
        print(_)
    select = input('\nВыбрать задачу (1-3) >: ')

    match select:
        case '1':
            task01()
        case '2':
            task02()
        case '3':
            task03()
        case _:
            print(f'task number {select} not found!')


def task01():
    '''Задайте натуральное число N. Напишите программу, которая составит 
    список простых множителей числа N. 60 -> 2, 2, 3, 5'''

    print('\nЗадача № 1')
    num = int(input('Задайте натуральное число >:'))
    result = []
    tst = num
    k = 2
    while tst > 1:
        if tst % k == 0:
            result.append(k)
            tst /= k
        else:
            k += 1

    print(*result)


def task02():
    '''Задача 2. В первой строке файла находится информация об ассортименте 
    мороженного, во второй - информация о том, какое мороженное есть на складе. 
    Выведите названия того товара, который закончился.
    Пример:
    1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
    2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
    Ответ. Закончилось: «Бурёнка»'''
    print('\nЗадача № 2')
    data = open('Мороженое.txt', mode="r", encoding="utf-8")
    base_str = data.readlines()
    data.close

    f_str = set(base_str[0].replace('\n', '').split(', '))
    s_str = set(base_str[1].replace('\n', '').split(', '))
    print(f'Закончилась {f_str.difference(s_str)}')


def task03():
    '''Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
    3 -> 3.142'''
    print('\nЗадача № 3')
    num_decimal = int(input('Число знаков десятичной дроби числа π >: '))
    print(round(pi, num_decimal))


def task04():
    '''Даны два файла, в каждом из которых находится запись многочлена. 
    Найдите сумму данных многочленов.
    1. 5x^2 + 3x
    2. 3x^2 + x + 8
    3. Результат: 8x^2 + 4x + 8'''
    pass


start_task()
