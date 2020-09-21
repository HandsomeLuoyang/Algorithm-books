class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k > n * n or k < n:
            return 0
        if k % n == 0:
            return 2 * self.c(k//n, n)
        
        flag = False
        
        for i in range(1, n+1):
            for j in range(i, n+1):
                if (i+j) * n - i*j == k:
                    row_1, row_2 = i, j
                    flag = True
                    break
        if not flag:
            return 0
            
        if row_1 == row_2:
            return self.c(row_1, n) * self.c(row_2, n)
        return 2 * self.c(row_1, n) * self.c(row_2, n)

    def c(self, m, n):
        top = 1
        bottom = 1
        for i in range(m):
            top *= n
            n -= 1
            bottom *= (i+1)
        return top // bottom


s = Solution()
print(s.paintingPlan(5, 9))
