class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        col = (len(s) // 2) + 1
        lst = ['' for _ in range(numRows)]
        row_index = 0
        direct = 1
        for one_s in s:
            if direct == 1:
                lst[row_index] += one_s
                row_index += 1
            else:
                lst[row_index] += one_s
                row_index -= 1
            if row_index == 0:
                direct = 1
            if row_index == numRows - 1:
                direct = 0

        return ''.join(lst)