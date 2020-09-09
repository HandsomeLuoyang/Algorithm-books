class Solution:
    def maxDotProduct(self, nums1: list, nums2: list) -> int:
        rows, columns = len(nums1), len(nums2)
        dp = [[-float('inf')] * (columns + 1) for _ in range(rows + 1)]
        for i in range(1, rows+1):
            for j in range(1, columns+1):
                dp[i][j] = nums1[i-1] * nums2[j-1]
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1], dp[i][j] + dp[i-1][j-1])
        return dp[rows][columns]

sol = Solution()
print(sol.maxDotProduct([1, 3, 4], [4, 5]))