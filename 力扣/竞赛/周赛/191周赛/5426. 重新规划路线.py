class Solution:
    def minReorder(self, n: int, connections: list) -> int:
        # 邻接矩阵
        matrix = [[0] * n for i in range(n)]
        for i in connections:
            matrix[i[0]][i[1]] = 1
        for i in range(n):
            matrix[i][i] = 1

        for i in matrix:
            for j in i:
                print(j, end=' ')
            print('')
        print('------'*5)

        ans = 0
        # 0能直接到达的地方，却不能到达0，就给它加一个方向
        for j in range(1, n):
            if matrix[0][j] == 1:
                if matrix[j][0] == 0:
                    matrix[j][0] = 1
                    ans += 1
        

        # 记录当前所有能到达1的点
        self.ok_list = []
        for i in range(1, n):
            if matrix[i][0] == 1:
                self.ok_list.append(i)
        
        # 广搜
        for i in self.ok_list:
            for j in range(1, n):
                if (matrix[i][j] == 1) and (not j in self.ok_list) and matrix[j][i] != 1:
                    matrix[j][i] = 1
                    for k in range(n):
                        if matrix[k][j] == 1:
                            self.ok_list.append(k)
                    ans += 1
                    self.ok_list.append(j)



        for i in matrix:
            for j in i:
                print(j, end=' ')
            print('')
        
        print(ans)
        return ans

sol = Solution()
sol.minReorder(5, [[1,0],[1,2],[3,2],[3,4]])