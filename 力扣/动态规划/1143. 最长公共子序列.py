class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 定义二位dp数组
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        # 遍历，状态转移
        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) if text2[i-1] != text1[j-1] else dp[i-1][j-1] + 1

        return dp[-1][-1]

        for i in dp:
            for j in i:
                print(j, end=' ')
            print('')


s = Solution()
print(s.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))
