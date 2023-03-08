import os
import numpy as np
import matplotlib.pyplot as plt
from random import randint as ri

os.system('clear')

def task01():
    #Построить график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30. 
    # По графику определить, при каких значения x значение функции отрицательно.
    dot_list = [5*x**2 + 10*x -30 for x in range(-5,5)]
    plt.axhline(0, color ='red')
    plt.plot(dot_list)
    plt.show()


def task02():
    # There are data on the area and cost of 15 houses. Риелтору требуется узнать 
    # в каких домах стоимость квадратного метра меньше 50000 рублей.
    # Предоставить графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади. 
    # Данные о домах сформируйте случайным образом. 
    # Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.
    def custom_key(data):
        # [0] - по номеру дома, [1]- по площади ,[2]- по стоимости,[3] - по цене за м.кв.
        return data[1]

    data_on_houses =[] # случайный список домов

    max_price = 50_000
    for id_home in range(1,16):
        cost_home = ri(3_000_000,20_000_000)
        area_home = ri(100,300)
        price_home = round(cost_home/area_home)
        data_on_houses.append((str(id_home).rjust(2,"0"),area_home,cost_home,price_home))
    
    data_on_houses.sort(key = custom_key) # сортировка по площади, не понял как это работает, но работает.

    plt.axhline(max_price, color ='red')
    plt.title(f'Красная линия - максимально \nдопустимая цена за кв.м. = {max_price}р.')   
    plt.bar(['№'+str(x[0]) for x in data_on_houses],[ y[3] for y in data_on_houses])
    
    plt.show()


def menu():
    print('''Выбор задачи:
    1 - Построить график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
    2 - Предоставить графические данные о стоимости квадратного метра каждого дома''')
    start = int(input('-->:'))
    match start:
        case 1:
           task01()
        case 2:
           task02()
        case _:
            pass  
menu()  
     