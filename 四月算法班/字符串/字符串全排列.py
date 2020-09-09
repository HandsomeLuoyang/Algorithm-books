# 递归方式实现全排列
# '1234'
# 核心在于'交换'
# 第一次将第一个和第一个本身进行交换，然后递归下去，变成第二个跟第二个本身交换。。。。。到最后一个
# 第二次将第一个和第二个进行交换，同样递归下去
# 每一次交换之后，再下次交换之前要再次交换回来，保证原顺序不变，以避免遗漏

# 下方这个是python内置库中的排列函数和组合函数，但是这里要自己实现，理解递归
# from itertools import permutations(排列函数), combinations(组合函数)
# ss = list(permutations(要排列的迭代对象：ss, 迭代数：4))

from numba import jit

@jit
def permutation(from_:int, to_:int):
    # 如果排到了第四个了，就直接打印输出
    if from_ == to_:
        print(''.join(ss_lst))
        pass
    for i in range(from_, to_):
        # 当前值和下一个值进行交换
        ss_lst[i], ss_lst[from_] = ss_lst[from_], ss_lst[i]
        # 当前值固定，让下一个值和下下个值进行交换，循而复之
        permutation(from_+1, to_)
        # print('交换前：', ss_lst)
        # 换回来，保证不遗漏
        ss_lst[i], ss_lst[from_] = ss_lst[from_], ss_lst[i]
        # print('交换后：', ss_lst)

        


# ss = input()
# ss_lst = list(ss)
# permutation(0, len(ss))


# ss_lst = [s for s in input().split()]
ss_lst = ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg", "vimw", "bxcb"]
permutation(0, len(ss_lst))