class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:
            return s
        ss = '#' + '#'.join(s) + '#'
        self.Manachar(ss)
        
        # m_value = max(self.mlc_lst)
        # m_index = self.mlc_lst.index(m_value)

        ans_str = ss[self.m_index-self.m_value+1:self.m_index+self.m_value]
        return ''.join(ans_str.split('#'))

    def Manachar(self, ss):
        # 字符串长度
        length = len(ss)
        # 建立马拉车数组
        self.mlc_lst = [0 for _ in range(length)]
        # 马拉差数组第一个为#，回文长度为其本身：1
        self.mlc_lst[0] = 1
        # 控制最远距离的index
        id_ = 0
        # 能控制到的最远距离
        mx = 1
        # 最大回文数值
        self.m_value = 0
        # 最大回文数值对应index
        self.m_index = -1
        # 开始遍历
        for i in range(1, length):
            if mx > i:
                self.mlc_lst[i] = min(self.mlc_lst[2*id_-i], mx-i)
            else:
                self.mlc_lst[i] = 1
            while i - self.mlc_lst[i] >= 0 and i + self.mlc_lst[i] <length and ss[i + self.mlc_lst[i]] == ss[i-self.mlc_lst[i]]:
                self.mlc_lst[i] += 1

            if self.mlc_lst[i] > self.m_value:
                self.m_value = self.mlc_lst[i]
                self.m_index = i

            if mx < i + self.mlc_lst[i]:
                id_ = i
                mx = i + self.mlc_lst[i]
        return self.mlc_lst