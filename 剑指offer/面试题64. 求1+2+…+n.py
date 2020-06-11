class Solution:
    def sumNums(self, n: int) -> int:
        self.ans = 0
        self.helper(n)
        return self.ans
        
    def helper(self, n:int):
        self.ans += n
        return n and self.helper(n - 1)