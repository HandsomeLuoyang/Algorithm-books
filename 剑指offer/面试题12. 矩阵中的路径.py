class Solution:
    def exist(self, board: list(list(str)), word: str) -> bool:
        # 这题使用DFS深度优先搜索加剪枝完成
        def dfs(i, j, k):
            """
            dfs深搜递归函数
            """
            # 定义边界
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[k] != board[i][j]:
                return False
            # 成功条件
            if k == len(word) - 1:
                return True
            # 每次从一个位置开始递归的时候将这个位置的字符设置为'\'，相当于标志着这个点已经访问过了
            tmp, board[i][j] = board[i][j], '1'
            # 从四个方向搜索递归出去
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            # 这个位置搜索之后要改回来，防止影响到后面的搜索
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False