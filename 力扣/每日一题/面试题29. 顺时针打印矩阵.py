class Solution:
    def spiralOrder(self, matrix: list) -> list:
        rows = len(matrix)
        if rows == 0:
            return []
        columns = len(matrix[0])
        if columns == 0:
            return []
        top, left, right, bottom = 0, 0, columns, rows
        ans_lst = []
        while True:
            if left == right:
                break
            for j in range(left, right):
                ans_lst.append(matrix[top][j])
            top += 1

            if top == bottom:
                break
            for i in range(top, bottom):
                ans_lst.append(matrix[i][right-1])
            right -= 1

            if right == left:
                break
            for j in range(right-1, left-1, -1):
                ans_lst.append(matrix[bottom-1][j])
            bottom -= 1

            if top == bottom:
                break
            for i in range(bottom-1, top-1, -1):
                ans_lst.append(matrix[i][left])
            left += 1
        return ans_lst