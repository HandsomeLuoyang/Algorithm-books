class Solution:
    def numWays(self, n: int) -> int:
        n = n + 1
        if n == 1 or n == 2:
            return 1
        self.m, self.n = 1, 1
        for i in range(n-2):
            self.m, self.n = self.n, self.m + self.n
        return self.n % 1000000007