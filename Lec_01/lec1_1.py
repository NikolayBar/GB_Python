import os
import random as r
os.system('clear')


# def changeIndexTuple(kr, indx, num):
#     lst = list(kr)
#     lst[indx] = num
#     kr = tuple(lst)
#     return kr


# kr = tuple(r.randint(0, 25) for i in range(10))
# indx, val = 3, 88

# result = changeIndexTuple(kr, indx, val)
# print(result)

# '''Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: 'Илья', 'Георгий', 'Лев', 'Демьян', 'Антон', 'Владислав', 'Боря', 'Стас', 'Марк', 'Влад'
# Сильные: 'Федор', 'Георгий', 'Олег', 'Демьян', 'Артем', 'Елисей', 'Боря', 'Стас', 'Влад' '''

# beauty = set(['Илья', 'Федор', 'Семен', 'Олег', 'Лев',
#               'Антон', 'Артем', 'Боря', 'Стас', 'Марк', 'Ян'])
# strong = set(['Илья', 'Георгий', 'Лев', 'Демьян', 'Антон',
#               'Владислав', 'Боря', 'Стас', 'Марк', 'Влад'])
# smart = set(['Федор', 'Георгий', 'Олег', 'Демьян',
#             'Артем', 'Елисей', 'Боря', 'Стас', 'Влад'])

# result = smart.intersection(strong.intersection(beauty))
# print(result)
rand_num_set = []
for _ in range(10):
    rand_num_set.append(r.randint(0, 20))
print(rand_num_set)
rand_num_set = set(rand_num_set)
print(rand_num_set)
