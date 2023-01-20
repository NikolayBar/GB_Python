import os
import random as r
os.system('clear')


def task02():
    data = open("Телефоны.txt", mode="r", encoding="utf-8")
    phones = data.readlines()
    data.close

    shop01 = set(phones[1].replace('\n', '').split(', '))
    shop02 = set(phones[3].removesuffix('\n').split(', '))
    shop02 = set(phones[5].removesuffix('\n').split(', '))

    print(*shop01)


# def task03():
#     '''Задача 2. В зоопарк отправили отчёт о новом поступлении зверей с ошибкой, в результате которой некоторые данные не расшифровались. Расшифруйте данные. Определите, в какой клетке находится лев. Номер клетки совпадает с номером строки. 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'''
#     find = 'барсук'
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     dic = []
#     result = []
#     for i in range(len(alphabet)):
#         x = str(bin(i))[2:].zfill(6)
#         dic.append([x] + [alphabet[i]])
#     dic = dict(dic)
#     data = open("Животные.txt", mode="r", encoding="utf-8")
#     lst = data.readlines()
#     data.close
#     lst = [s.replace('\n', '') for s in lst]

#     for el in lst:
#         name = ''
#         for i in range(0, len(el), 6):
#             name = name + dic[el[i: i+6]]
#         result.append(name)

#     if find in result:
#         print(f'{find} живет в клетке № {result.index(find)}')
#     else:
#         print(f'{find} не значится в списке')


# task03()
