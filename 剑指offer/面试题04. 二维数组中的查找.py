import time


class Solution:
    def findNumberIn2DArray(self, matrix: list(list()), target: int) -> bool:
        if len(matrix) < 1 or len(matrix[0]) == 0:
            return False
        row = len(matrix)
        column = len(matrix[0])

        # 对每一行使用二分查找
        # for i in range(row):
        #     lo = 0
        #     hi = column - 1
        #     while lo <= hi:
        #         mid = (lo + hi) // 2
        #         if matrix[i][mid] < target:
        #             lo = mid + 1
        #         elif matrix[i][mid] > target:
        #             hi = mid - 1
        #         else:
        #             return True
        # return False


        # 暴力搜索
        # for i in matrix:
        #     for j in i:
        #         if j == target:
        #             return True
        #         if j > target:
        #             break
        # return False

        # 以右上角为基点，构造一个二分查找树
        i = 0
        j = column - 1
        while True:
            if i == row or j == -1:
                return False
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True

        
s = Solution()
matrix = []
tmp_lst = []
for i in range(1, 10000000):
    tmp_lst.append(i)
    if i % 100000 == 0:
        matrix.append(tmp_lst[:])
        tmp_lst.clear()

st = time.process_time()
print(s.findNumberIn2DArray(matrix, 9500000))
ed = time.process_time()
print(ed - st)