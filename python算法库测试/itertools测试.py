# from itertools import product, permutations, combinations, combinations_with_replacement
# from functools import cmp_to_key
# import collections

# # 相当于嵌套的for， 对两个列表进行组合
# for i,j in product([1,2,3],[4,5]):
#     print(i,j)

# # 对一个列表进行全排列，返回全排列列表
# print(list(permutations([1,2,3])))

# # 对一个列表进行组合，返回列表的组合列表， 第一个参数为一个迭代器，第二个参数为从中选出几个数进行组合
# print(list(combinations([1,2,3],2)))

# # 在排列的基础上，同一个元素可以组合自身
# print(list(combinations_with_replacement('ABCD', 2)))

# lst = [i for i in range(10)]
# for index, val in enumerate(lst):
#     print(index, val)


# def custom_sort(x,y):
#     if x>y:
#         return -1
#     if x<y:
#         return 1
#     return 0

# lst = [i for i in range(10, -1, -1)]
# print(lst)

# lst.sort()
# print(lst)

# print(sorted(lst, key=cmp_to_key(custom_sort)))

# d = dict(collections.Counter('Hello World'))
# print(d)
# print(sorted(d.items(), key=lambda x: x[1], reverse=True))


# lst = [1, 2, 3, 4, 5, 6]
# lst = [i for i in lst if i % 2 != 0]

# print(lst)

d = {1:3, 2:5}
print(d.get(4, 1))