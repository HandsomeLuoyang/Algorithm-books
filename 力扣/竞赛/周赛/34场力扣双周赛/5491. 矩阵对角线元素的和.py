class Solution:
    def diagonalSum(self, mat) -> int:
        length = len(mat)
        ans = 0
        for i in range(length):
            ans += mat[i][i]
        j = 0
        for i in range(-1, -length-1, -1):
            ans += mat[i][j]
            j += 1
        if length % 2 != 0:
            ans -= mat[length//2][length//2]
        return ans

s = Solution()
print(s.diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]))