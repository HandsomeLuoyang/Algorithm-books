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
