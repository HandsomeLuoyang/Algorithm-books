# 给定一个字符串S[...N-1]，要求把S的前k个字符移动到S的尾部，如把字符串"abcdef"
# 前面的2个字符'a'、'b' 移动到字符串的尾部，得到新字符串"cdefab":即字符串循环
# 左移k。

# 算法：三次洗牌算法 (X'Y')' == YX

# 由于python里面字符串为不可变类型，无法原地修改，此处转成列表
ss = input()

ss_lst = list(ss)

def reverse_string(lst:list, _from, _to):
    while _from < _to:
        t = lst[_from]
        lst[_from] = lst[_to]
        _from += 1
        lst[_to] = t
        _to -= 1



def left_rotate_string(lst:list, n, m):
    m %= n
    reverse_string(lst, 0, m-1)
    reverse_string(lst, m, n-1)
    reverse_string(lst, 0, n-1)

m = int(input())
left_rotate_string(ss_lst, len(ss_lst), m)
print(ss_lst)