class Solution:
    def maxValue(self, grid: list) -> int:
        grid.insert(0, [0] * len(grid[0]))
        for i in range(len(grid)):
            grid[i].insert(0, 0)

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = max(grid[i-1][j] + grid[i][j], grid[i][j-1] + grid[i][j])
        
        return grid[-1][-1]