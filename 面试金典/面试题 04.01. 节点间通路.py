class Solution:
    def findWhetherExistsPath(self, n: int, graph: list, start: int, target: int) -> bool:
        matrix = [[0 for i in range(n)] for i in range(n)]
        for path in graph:
            matrix[path[0]][path[1]] = 1

        self.flag = 0
        visited = set()
        visited.add(start)

        def dfs(start: int, target: int):
            for i in range(0, n):
                if i not in visited:
                    if matrix[start][i] == 1:
                        if i == target:
                            self.flag = 1
                            return self.flag
                        else:
                            visited.add(i)
                        flag = dfs(i, target)
                        if flag:
                            return flag
        dfs(start, target)
        return True if self.flag else False


s = Solution()
print(s.findWhetherExistsPath(25, [[0, 1], [0, 3], [0, 10], [0, 18], [1, 2], [1, 7], [1, 11], [1, 12], [2, 4], [2, 5], [2, 13], [2, 16], [
      3, 6], [3, 8], [4, 9], [5, 17], [7, 20], [7, 22], [8, 10], [10, 19], [11, 15], [13, 14], [14, 21], [15, 23], [19, 24], [20, 22]], 0, 12))
