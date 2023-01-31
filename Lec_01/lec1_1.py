def task01():
    number = [
        [1,20,3,5],
        [0,63,8,44],
        [3,51,7,99]
        ]
    num_uni =[]
    for i in number:
        num_uni += i
    number = sorted(list(set(num_uni)))
    print(number)
    print(number[1],number[-2])
    print(f'{number[-2]} - {number[1]} = {number[-2]-number[1]}')

number = [
    [1,20,3,5],
    [0,63,8,44],
    [3,51,7,99]
    ]
res=[]
max_num = max(number)
for i in range(len(number)):
    for j in number[i]:
        # if number[i][j] == max_num:
        print (j, ' ',max_num)

print(res)

    