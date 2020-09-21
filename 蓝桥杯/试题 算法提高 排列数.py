from itertools import permutations

n = int(input())
num_lst = [str(i) for i in range(10)]


index = 1
for i in permutations(num_lst, 10):
    if index == n:
        print(''.join(i))
    if index > n:
        break
    index += 1