from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        if len(s) < len(p):
            return []

        ans_lst = []
        c = Counter(p)
        # 需求字典
        need_dict = dict(c)
        need_len = len(need_dict)

        # 这个移动窗口的长度固定为p的长度，只需要左右边框一边向右移动，一边判断框内的数据是否符合要求就行
        left = 0
        right = len(p)
        valid = 0

        # 当前字典及初始化
        now_dict = {}
        for i in p:
            now_dict[i] = 0
        for i in s[left:right]:
            if i in need_dict:
                now_dict[i] += 1
                if now_dict[i] == need_dict[i]:
                    valid += 1

        s += '\0'
        # 窗口开始移动
        while right < len(s):
            # 如果符合要求就直接放入答案数组
            if valid == need_len:
                ans_lst.append(left)

            # 左窗口右移
            c = s[left]
            if c in now_dict:
                if now_dict[c] == need_dict[c]:
                    valid -= 1
                now_dict[c] -= 1
            left += 1

            # 右窗口右移
            c = s[right]
            if c in need_dict:
                now_dict[c] += 1
                if now_dict[c] == need_dict[c]:
                    valid += 1
            right += 1

        return ans_lst

s = Solution()


import time
import random
st = time.process_time()
ss = ''.join([chr(random.randint(97, 122)) for _ in range(10000000)])
ed = time.process_time()
print('耗费时间: {}'.format(ed-st))


st = time.process_time()
print(s.findAnagrams(ss, 'acdeaoifjodajsoifjoadfasdfasdfwafweafewqfwefwqfqwefdafdadzcvxc'))
ed = time.process_time()

print('耗费时间: {}'.format(ed-st))