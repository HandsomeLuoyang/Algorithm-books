class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # 首先特判一下，若是K能被2，5整除，则肯定无解
        if not K%2 or not K%5:
            return -1
        
        index = 1
        num = 1

        while num % K:
            num = 10*num + 1
            index += 1
        
        return index

s = Solution()
print(s.smallestRepunitDivByK(17))