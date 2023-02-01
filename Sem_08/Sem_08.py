import os
from random import randint as ri
os.system('clear')

def aver(a):
    return sum(a)/len(a)
def print_list(lst):
    for _ in lst:
        print(*_)

def start_task():     
    decription = [
        '1. Определить группу с наилучшим средним баллом',
        '2. Определить, сумма элементов каких строк превосходит сумму главной диагонали матрицы',
        '3. Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца.'
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
    # Задача 1. В каждой группе учится от 20 до 30 студентов. 
    # По итогам экзамена все оценки заносятся в таблицу. 
    # Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
    print (f'ЗАДАЧА 01\n')
    num_group = 5 # число групп
    kurs = []
    res =[]
    for _ in range(num_group):
        num_stud = ri(5,6)# число студентов в группе min,max
        x = [ ri(2,5) for x in range(num_stud)]
        
        print(f'группа {_+1}, баллы :{(x)};\tсредний {round(aver(x),3)}')
        kurs.append(x)
    
    for _ in kurs:
        res.append(round(aver(_),4))
    best = max(res)
    print(f'\nлучшая группа - {res.index(best)+1}-я, средний балл : {best}')

def task02():
    # Задача 2. Дана квадратная матрица, заполненная случайными числами. 
    # Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
    N = 5
    print(f'ЗАДАЧА 02\nматрица {N}x{N}\n')
    matrx =[]
    sum_row =[]
    for _ in range(N):
        sum_diag =[ ri(1,9) for x in range(N)]
        matrx.append(sum_diag)

    print_list(matrx)
    sum_diag = sum([matrx[_][_] for _ in range(N)])
    for i in range(N):
        x = sum(matrx[i])
        if  x > sum_diag:
            sum_row.append(i)
    
    if len(sum_row) == 1:
        print(f'\nСумма значений строки : {sum_row}\nбольше суммы (={sum_diag}) главной диагонали')
    elif len(sum_row) > 1:
        print(f'\nСумма значений строк : {sum_row}\nбольше суммы (={sum_diag}) главной диагонали')
    else:
        print(f'\nСтрок сумма которых превышает сумму главной диагонали нет')

def task03():
    # Задача 3. В двумерном массиве хранятся средние дневные температуры 
    # с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка.
    # Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. 
    # Выведите их даты.
    pass

def task04():
    # Задача 4* (Дополнительная). Реализуйте игру «Поле чудес». 
    # Вопрос и правильный ответ сохраните в файл. 
    # Реализуйте алгоритм шифрования правильного ответа.
    pass

# start_task()
task02()