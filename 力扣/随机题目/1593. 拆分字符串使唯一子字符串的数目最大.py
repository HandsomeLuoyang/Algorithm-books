class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        self.max_length = -1

        def dfs(left: int, seen: set, length: int):
            if left == len(s):
                self.max_length = self.max_length if self.max_length > length else length
            for right in range(left+1, len(s)+1):
                if not s[left:right] in seen:
                    seen.add(s[left:right])
                    dfs(right, seen, length+1)
                    seen.remove(s[left:right])
            

        for i in range(1, len(s)+1):
            seen.add(s[0:i])
            dfs(i, seen, 1)
            seen.remove(s[0:i])
        
        return self.max_length

s = Solution()
print(s.maxUniqueSplit('aa'))
