import os
import random as r
os.system('clear')


def start_task():
    decription = [
        '1. Вывести из списка числа  больше 5',
        '2. Создайть из списка случайную возрастающую последовательность',
        '3. Удалить все повторяющиеся элементы'
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
    # Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
    # Используйте для решения лямбда-функцию.
    # 2, 3, 4, 6, 7, 8 -> 6, 7, 8'''
    print('\nЗадача № 1')
    lst = [r.randint(1, 10) for _ in range(10)]
    res = [x for x in lst if x > 5]
    print(f'Исходный список \t: {lst}')
    print(f'Значения больше 5 \t: {res}')


def task02():
    # Дан список случайных чисел. Создайте список, в который попадают числа,
    # описывающие случайную возрастающую последовательность.
    # Порядок элементов менять нельзя.
    # [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

    print('\nЗадача № 2')

    lst = [r.randint(0, 50) for _ in range(10)]
    res = []
    el_pos = r.randint(0, len(lst)//2)  # начальный индекс
    s_stp = r.randint(1, len(lst)//2)  # случайный шаг
    next = el_pos+s_stp
    res.append(lst[el_pos])

    while next < len(lst):
        if res[-1] < lst[next]:
            res.append(lst[next])
            next += s_stp
        else:
            next += 1

    print(f'исходный список: {lst}')
    print(f'возрастающая последовательность: {res}\n')


def task03():
    # Задайте список случайных чисел от 1 до 10.
    # Посчитайте, сколько всего совпадающих элементов есть в списке.
    # Удалите все повторяющиеся элементы.
    # [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
    # Список уникальных элементов [1, 4, 2, 3, 6, 7]

    print('\nЗадача № 3')
    lst = []
    for i in range(10):
        lst.append(r.randint(1, 9))
    lst.sort()
    unq = set(lst)
    unq_num = 0
    for x in unq:
        if lst.count(x) > 1:
            unq_num += lst.count(x)

    print(f'В списке {lst} совпадают {unq_num} элем.')
    print(f'Список уникальных значенй: {list(unq)} ')


start_task()
