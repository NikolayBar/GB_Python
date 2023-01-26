# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

user_in = input('натуральное число N ->:')
rep_num = 3
num_lst = []
for i in range(1, rep_num+1):
    num_lst.append(int(user_in*i))

print(*num_lst, sep=' + ', end=' = ')
print(sum(num_lst))
