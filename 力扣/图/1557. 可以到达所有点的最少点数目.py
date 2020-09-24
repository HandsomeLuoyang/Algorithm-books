class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list) -> list:
        indeg = [0] * n
        for item in edges:
            # 记录入读节点个数
            indeg[item[1]] += 1
        
        q = [u for u in range(n) if indeg[u] == 0]
        return q