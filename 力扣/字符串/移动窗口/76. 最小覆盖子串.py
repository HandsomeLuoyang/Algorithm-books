from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_length, t_length = len(s), len(t)

        if s_length < 1 or s_length < t_length:
            return ''

        c = Counter(t)
        need_dict = dict(c)
        need_size = len(need_dict)
        now_dict = {}

        left = 0
        right = 0
        valid = 0
        start = -1
        length = 10000000
        while right < s_length:
            # c是移入的字符
            c = s[right]
            # 窗口右侧向右扩张
            right += 1
            # 更新数据
            if c in need_dict:
                if c in now_dict:
                    now_dict[c] += 1
                else:
                    now_dict[c] = 1
                if now_dict[c] == need_dict[c]:
                    valid += 1
            
            # 判断左侧是否需要收缩 
            while valid == need_size:
                # 计算窗口距离
                if right - left < length:
                    start = left
                    length = right - left
                c = s[left]
                # 窗口左框右移
                left += 1
                if c in need_dict:
                    if now_dict[c] == need_dict[c]:
                        valid -= 1
                    if now_dict[c] != 0:
                        now_dict[c] -= 1
        return '' if start == -1 else s[start:start + length]

s = Solution()
print(s.minWindow('ADOBECODEBANC', 'ABC'))
