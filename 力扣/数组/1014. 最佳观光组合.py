class Solution:
    def maxScoreSightseeingPair(self, A: list) -> int:
        """动态规划"""
        fn = 0
        an = A[0] + 0
        for i in range(len(A)-1):
            tmp_an = A[i] + i
            an = an if an > tmp_an else tmp_an
            tmp_fn = an + A[i+1]-i-1
            fn = fn if fn > tmp_fn else tmp_fn
        return fn

s = Solution()
print(s.maxScoreSightseeingPair([8,1,5,2,6]))