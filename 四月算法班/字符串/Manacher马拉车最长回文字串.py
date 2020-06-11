# 给定一个字符串，求出其最长回文子串。例如：
# s="abcd"，最长回文长度为 1；
# s="ababa"，最长回文长度为 5；
# s="abccb"，最长回文长度为 4，即 bccb。
# 以上问题的传统思路大概是，遍历每一个字符，以该字符为中心向两边查找。其时间复杂度为O(n^2)，效率很差。
# 1975年，一个叫Manacher的人发明了一个算法，Manacher 算法（中文名：马拉车算法），该算法可以把时间复杂度提升到O(n)。下面来看看马拉车算法是如何工作的。

# 与kmp算法相似之处是，马拉车算法也需要利用已知信息来部分推出更多的信息以简化计算，优化时间复杂度
import os

def Manachar(ss):
    # 字符串长度
    length = len(ss)
    # 建立马拉车数组
    mlc_lst = [0 for _ in range(length)]
    # 马拉差数组第一个为#，回文长度为其本身：1
    mlc_lst[0] = 1
    # 控制最远距离的index
    id_ = 0
    # 能控制到的最远距离
    mx = 1
    # 开始遍历
    for i in range(1, length):
        if mx > i:
            mlc_lst[i] = min(mlc_lst[2*id_-i], mx-i)
        else:
            mlc_lst[i] = 1
        while i - mlc_lst[i] >= 0 and i + mlc_lst[i] <length and ss[i + mlc_lst[i]] == ss[i-mlc_lst[i]]:
            mlc_lst[i] += 1
        if mx < i + mlc_lst[i]:
            id_ = i
            mx = i + mlc_lst[i]
    return mlc_lst



ss = input()
ss = '#' + '#'.join(ss) + '#'
mlc_lst = Manachar(ss)
print(ss)
print(mlc_lst)

m_value = max(mlc_lst)
m_index = mlc_lst.index(m_value)

# side = (m_value) // 2
ans_str = ss[m_index-m_value+1:m_index+m_value]
print(''.join(ans_str.split('#')))

