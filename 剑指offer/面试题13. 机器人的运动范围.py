class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 深度优先搜索函数
        visited = set()

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or self.get_sum(i, j) > k or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)

    def get_sum(self, i: int, j: int):
        num_str = str(i) + str(j)
        sum_ = 0
        for k in num_str:
            sum_ += int(k)
        return sum_
