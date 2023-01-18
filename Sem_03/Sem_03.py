import os
from datetime import date as dt
os.system('clear')


def task01():
    '''Задача 1. Создайте файл. Запишите в него N первых элементов 
    последовательности Фибоначчи.  6 -> 1 1 2 3 5 8'''
    n = 8
    num_fib = ''
    lst = [1, 1]
    for i in range(2, n):
        lst.append(lst[-1] + lst[i-2])

    for s in lst:
        num_fib += str(s)+' '

    data = open("task01.txt", mode="w", encoding='utf-8')
    data.writelines(num_fib)
    data.close


def task02():
    '''Задача 2. В файле находятся названия фруктов. Выведите все фрукты, 
    названия которых начинаются на заданную букву. а -> абрикос, авокадо, апельсин, айва.'''
    symb_in = input('Введите начальную букву :')
    if len(symb_in) > 1:
        symb_in = symb_in[0]
    data = open('task02.txt', mode='r', encoding='utf-8')
    lst = data.readlines()
    result = []
    data.close
    for current_word in lst:
        if current_word[0].lower() == symb_in.lower():
            result.append(current_word.rstrip('\n'))
    if len(result) == 0:
        print(f'Увы, на букву {symb_in} ничего не нашлось!')
    else:
        print(*result)


def task03():
    '''Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.'''
    print(dt.today())
    bot_name = 'HW-003'
    dic_bot = {'привет': 'Здрасте!',
               'как тебя зовут': f'Меня зовут {bot_name}-й.',
               'какое сегодня число': f'Сегодня {dt.today()}',
               'что ты умеешь': 'Пока очень мало.'
               }
    bSymb = ('?', '.', '!', ',')
    flag = True
    while flag:
        user_in = input(' >:')
        if user_in != "":

            answ = dic_bot.get(user_in.lower())
            if answ != None:
                print(answ)
            else:
                print(f'Не понял, это про что -"{user_in}"?')
        else:
            flag = False
    print('Пока!')


# task01()
# task02()
# task03()
