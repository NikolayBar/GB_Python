import os
import numpy as np
from pprint import pprint as prnt
os.system('clear')

# size = (4,4)

# matrix = np.random.randint(10,99,size)
# print(matrix)
# # num_dict ={}
# # for row in matrix:
# #     for num in row:
# #         if num in num_dict.keys():
# #             num_dict[num] +=1
# #         else:
# #             num_dict[num] = 1

# # value = list(num_dict.values())
# # max_val = np.max(value)
# # for key in num_dict.keys():
# #     if num_dict[key] == max_val:
# #         print(f'частый эл. {key} {max_val}')
# uniq_el, counts = np.unique(matrix, return_counts=True)
# print(uniq_el)
# print(counts)

size = (5,5)
matrix = np.random.randint(0,2,size)

print(matrix)

result = ~(matrix.any(axis=0))
if True in result:
    print(f' нулевой столбец {np.argmax(result)+1}')

print(result)