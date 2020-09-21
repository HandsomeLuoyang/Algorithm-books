class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        visited = set()
        max_length = 0
        cur_length = 0
        for i in range(len(s)):
            if s[i] not in visited:
                cur_length += 1
                max_length = max_length if max_length > cur_length else cur_length
            else:
                max_length = max_length if max_length > cur_length else cur_length
                cur_length = 1
                visited.clear()
            visited.add(s[i])
        return max_length
s = Solution()
print(s.lengthOfLongestSubstring('dvdf'))