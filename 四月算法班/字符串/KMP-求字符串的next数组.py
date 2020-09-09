# 这里是kmp算法最核心也是最难得一步，求出模式字符串的next数组，讲白了next数组就是
# 模式字符串的自我认识，为了在匹配字符串的时候一遍过，模式字符串必须明白自己哪些部位是相同的
# 是可以直接跳过去的。

# 'abcabde'
def get_next_lst(ss: str) -> list:
    length = len(ss)
    next_lst = [0 for _ in range(length)]
    next_lst[0] = -1
    i = 0
    j = -1
    while i < length - 1:
        if j == -1 or ss[i] == ss[j]:
            i += 1
            j += 1
            # 对next数组进行优化
            # 若 pattern[i] == pattern[j]并且ss[i]==ss[j]的话
            # 那么其实当发生不匹配的时候，可以不移动到next[j]
            # 而是直接移动到next[next[j]]因为不匹配的字符与ss[i]不等
            # 而ss[i]又与ss[j]相等
            # 因此不匹配的字符肯定与ss[j]不想等
            # if ss[i] == ss[j]:
            #     next_lst[i] = next_lst[j]
            # else:
            #     next_lst[i] = j
            next_lst[i] = j
        else:
            j = next_lst[j]
    return next_lst

print(get_next_lst('aadaaddcd'))