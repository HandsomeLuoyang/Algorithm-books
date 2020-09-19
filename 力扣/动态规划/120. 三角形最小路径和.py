class Solution:
    def minimumTotal(self, triangle: list) -> int:
        # 递归函数写法
        # def helper(n: int, m: int):
        #     if n >= len(triangle):
        #         return 0
        #     return min(helper(n+1, m), helper(n+1, m+1)) + triangle[n][m]

        # return helper(0, 0)

        # 动态规划版
        #TODO:优化空间为线性，因为只需要两层的数据就可以不断往下递推
        dp = [[0 for _ in range(len(triangle[-1])+1)] for _ in range(len(triangle)+1)]
        for i in range(0, len(triangle)):
            for j in range(0, i+1):
                if j == 0:
                    dp[i+1][j+1] = dp[i][j+1] + triangle[i][j]
                elif j >= i:
                    dp[i+1][j+1] = dp[i][j] + triangle[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1]) + triangle[i][j]
        
        return min(dp[-1][1:])
        
        # for i in dp:
        #     for j in i:
        #         print(j, end=' ')
        #     print('')


s = Solution()
print(s.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
