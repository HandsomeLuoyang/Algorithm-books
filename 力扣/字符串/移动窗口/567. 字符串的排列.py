from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c = Counter(s1)
        # 需求字典
        need_dict = dict(c)
        need_len = len(need_dict)

        # 这个移动窗口的长度固定为p的长度，只需要左右边框一边向右移动，一边判断框内的数据是否符合要求就行
        left = 0
        right = len(s1)
        valid = 0

        # 当前字典及初始化
        now_dict = {}
        for i in s1:
            now_dict[i] = 0
        for i in s2[left:right]:
            if i in need_dict:
                now_dict[i] += 1
                if now_dict[i] == need_dict[i]:
                    valid += 1

        s2 += '\0'
        # 窗口开始移动
        while right < len(s2):
            if valid == need_len:
                return True

            # 左窗口右移
            c = s2[left]
            if c in now_dict:
                if now_dict[c] == need_dict[c]:
                    valid -= 1
                now_dict[c] -= 1
            left += 1

            # 右窗口右移
            c = s2[right]
            if c in need_dict:
                now_dict[c] += 1
                if now_dict[c] == need_dict[c]:
                    valid += 1
            right += 1

        return False

s = Solution()
print(s.checkInclusion('ab', 'devbac'))