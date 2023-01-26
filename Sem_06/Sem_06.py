import os
import random as r
from math import gcd
os.system('clear')


def start_task():
    decription = [
        '1. Найдите значение выражения: N + NN + NNN',
        '2. Определить, есть в массиве последовательность из трёх элементов',
        '3. Найдите все простые несократимые дроби, лежащие между 0 и 1'
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
    # Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
    # N может быть любой длины.
    # N = 132: 132 + 132132 + 132132132 = 132264396
    pass


def task02():
    # Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число.
    # Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
    # [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
    # [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

    lst = [str(r.randint(0, 9)) for x in range(0, 15)]
    res_lst = ''.join(lst)
    print(res_lst)
    user_in = int(input('Введите трехзначное число ->:'))
    user_st = list(str(user_in))
    ln_in = len(user_st)
    res = f'Последовательность {user_in} не найдена'
    i = 0
    while i < len(lst)-(ln_in-1):
        if user_st == lst[i:i+ln_in]:
            res = f'Последовательность {user_in} найдена'
            print('\nСписок: ', end='')
            print(res_lst)
            print('        ' + ' '*i + '^'*ln_in)
            print(res)
            break
        i += 1
    else:
        print('\nСписок: ', end='')
        print(res_lst)
        print(res)


def task03():
    # Найдите все простые несократимые дроби, лежащие между 0 и 1,
    # знаменатель которых не превышает 11.
    # Несократимая дробь – это дробь, в которой числитель и знаменатель являются
    # взаимно простыми числами (имеют только один общий делитель – 1).
    pr_num = [x for x in range(1, 12)]
    res = []
    lst = []
    [[res.append((x, y)) for x in pr_num if x < y] for y in pr_num]
    for el in res:
        if gcd(el[0], el[1]) == 1:
            lst.append(str(el[0])+'/'+str(el[1]))
    print('Несократимые дроби с числителем не превышающем 11 :')
    print(*lst[:len(lst)//2])
    print(*lst[len(lst)//2:])


start_task()
