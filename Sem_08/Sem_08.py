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
    N = ri(3,6)
    print(f'ЗАДАЧА 02\nматрица {N}x{N}\n')
    matrx =[]
    sum_row =[]
    for _ in range(N):
        sum_diag =[ ri(10,99) for x in range(N)]
        matrx.append(sum_diag)

    print_list(matrx)
    sum_diag = sum([matrx[_][_] for _ in range(N)])
    for i in range(N):
        x = sum(matrx[i])
        if  x > sum_diag:
            sum_row.append(i)
    
    if len(sum_row) == 1:
        print(f'\nСумма значений строки : {sum_row}\nбольше суммы (равна {sum_diag}) главной диагонали')
    elif len(sum_row) > 1:
        print(f'\nСумма значений строк : {sum_row}\nбольше суммы (равна {sum_diag}) главной диагонали')
    else:
        print(f'\nСтрок сумма которых превышает сумму главной диагонали нет')

def task03():
    # Задача 3. В двумерном массиве хранятся средние дневные температуры 
    # с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка.
    # Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. 
    # Выведите их даты.
    def min_diap(data, dig):
        minimum = sum(data[0:dig])
        stop = len(data) - (dig-1)
        for  i in range(stop):
            if sum(data[i:i+dig]) < minimum:
                minimum = sum(data[i:i+dig])
                index = i
        return (index+1,index+dig)


    def max_diap(data,dig):
        maximum = sum(data[0:dig])
        stop = len(data) - (dig-1)
        for  i in range(stop):
            if sum(data[i:i+dig]) > maximum:
                maximum = sum(data[i:i+dig])
                index = i
        return (index+1,index+dig)
    days = 7
    name_month = ('МАЙ','ИЮНЬ','ИЮЛЬ','АВГУСТ','СЕНТЯБРЬ')
    log =(
        (13,14,18,8,9,16,18,19,7,6,18,22,16,15,16,13,11,15,14,12,15,12,14,7,13,20,13,14,11,20,16),
        (24,25,17,21,17,21,20,23,27,25,21,23,22,26,18,21,20,20,23,19,15,21,24,26,28,30,32,25,23,24),
        (22,25,29,30,24,29,31,23,22,29,32,25,23,23,23,22,21,20,20,20,21,25,28,28,27,29,31,27,23,22,23),
        (25,26,29,28,29,31,24,20,21,24,25,26,28,28,28,28,29,30,26,19,26,30,32,31,31,30,31,30,25,27,18),
        (13,11,15,14,11,10,9,10,12,15,15,14,14,13,12,16,16,13,10,14,14,12,14,9,7,10,12,10,12,17)
    )# данные за 2022 год
    print('ЗАДАЧА 03')
    print(f'самый жаркий и самый холодный {days}-дневный промежуток')
    for m in range(len(name_month)):
        print(f'{name_month[m]}\n  Самые холодные {days} дней: с {min_diap(log[m],days)[0]} по {min_diap(log[m],days)[-1]}')
        print(f'  Самые  жаркие  {days} дней: с {max_diap(log[m],days)[0]} по {max_diap(log[m],days)[-1]}')

def task04():
    # Задача 4* (Дополнительная). Реализуйте игру «Поле чудес». 
    # Вопрос и правильный ответ сохраните в файл. 
    # Реализуйте алгоритм шифрования правильного ответа.
    pass

start_task()
