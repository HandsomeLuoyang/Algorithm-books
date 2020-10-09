from typing import *
from collections import defaultdict, deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 记录出度边
        edges = defaultdict(list)
        # 访问记录
        visited = [0] * N
        visited[K-1] = 1
        # 记录边权重
        weights = defaultdict(int)

        for item in times:
            edges[item[0]].append(item[1])
            weights[(item[0], item[1])] = item[2]
        
        # 所花费时间
        cost_time = 0

        # Prime 算法 最小生成树
        q = deque([K])
        while q:
            tmp_node = q.popleft()
            tmp_time = 0
            for i in edges[tmp_node]:
                if not visited[i-1]:
                    visited[i-1] = 1
                    tmp_time = weights[(tmp_node, i)] if weights[(tmp_node, i)] > tmp_time else tmp_time
                    q.append(i)
            cost_time += tmp_time
        
        return cost_time if len(set(visited)) == 1 else -1
        

        

s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
