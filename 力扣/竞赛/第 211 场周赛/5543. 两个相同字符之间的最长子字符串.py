from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = defaultdict(lambda : -1)
        max_length = -1
        for index, value in enumerate(s):
            if seen[value] == -1:
                seen[value] = index
            else:
                tmp_length = index - seen[value] - 1
                max_length = tmp_length if tmp_length > max_length else max_length
        return max_length

s = Solution()
print(s.maxLengthBetweenEqualCharacters("cbzxy"))