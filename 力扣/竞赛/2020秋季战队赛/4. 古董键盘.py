from itertools import combinations, permutations
class Solution:
    def keyboard(self, k: int, n: int) -> int:
        return (len(set(list(permutations([chr(x) for x in range(ord('a'), ord('z')+1)]*k, n)))) % 1000000007)

s = Solution()
print(s.keyboard(5, 3))