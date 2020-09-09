class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right = 0, k
        yuan_set = set({'a', 'e', 'i', 'o', 'u'})
        ans = 0
        # 第一次扫描
        for i in s[left:right]:
            if i in 'aeiou':
                ans += 1
        tmp_ans = ans

        while right < len(s):
            if s[right] in yuan_set:
                tmp_ans += 1
            if s[left] in yuan_set:
                tmp_ans -= 1
            
            left, right = left + 1, right + 1

            if tmp_ans > ans:
                ans = tmp_ans
        return ans

s = Solution()
print(s.maxVowels('abciiidef', 3))