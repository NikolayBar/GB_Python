import os
os.system('clear')


def start_task():
    select = input('Select task Sem_04 (1-4) >: ')
    match select:
        case '1':
            task01()
        case '2':
            task02()
        case '3':
            task03()
        case '4':
            task04()
        case _:
            print(f'task number {select} not found!')


def task01():
    '''Задайте натуральное число N. Напишите программу, которая составит 
    список простых множителей числа N. 60 -> 2, 2, 3, 5'''
    pass


def task02():
    '''Задача 2. В первой строке файла находится информация об ассортименте 
    мороженного, во второй - информация о том, какое мороженное есть на складе. 
    Выведите названия того товара, который закончился.
    Пример:
    1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
    2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
    Ответ. Закончилось: «Бурёнка»'''
    pass


def task03():
    '''Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
    3 -> 3.142'''
    pass


def task04():
    '''Даны два файла, в каждом из которых находится запись многочлена. 
    Найдите сумму данных многочленов.
    1. 5x^2 + 3x
    2. 2. 3x^2 + x + 8
    3. Результат: 8x^2 + 4x + 8'''
    pass


start_task()
