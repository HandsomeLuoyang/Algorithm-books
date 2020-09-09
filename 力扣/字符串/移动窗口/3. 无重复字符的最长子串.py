class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口，用哈希集合
        occ = set()
        ans = 0
        st = 0
        # 遍历每个字符，做为回文串的开头
        n = len(s)
        for i in range(n):
            # 每搜索完一个字符，滑动窗口右移一位,集合移除前一个字符
            if i > 0:
                occ.remove(s[i-1])
            # 搜索无重复子串，改变窗口大小
            while st < n and s[st] not in occ:
                occ.add(s[st])
                st = st + 1
            ans = max(ans,len(occ))
        return ans