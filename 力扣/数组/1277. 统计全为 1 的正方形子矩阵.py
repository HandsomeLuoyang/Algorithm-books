class Solution:
    def countSquares(self, matrix) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        ans = 0
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    continue
                elif i == 0 or j == 0:
                    ans += 1
                else:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                    ans += matrix[i][j]
        print(matrix)
        return ans