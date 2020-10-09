from typing import *
from collections import defaultdict, deque
class Solution:
    def eventualSafeNodes(self, graph: list) -> list:
        # 存储入度边
        edges = defaultdict(list)
        # 存储每条边的出度
        chudu = [0] * len(graph)
        for i in range(len(graph)):
            for item in graph[i]:
                edges[item].append(i)
            chudu[i] += len(graph[i])
        
        # 从出度为0的点开始放入队列当中
        q = deque([i for i in range(len(chudu)) if chudu[i] == 0]) 

        ans_lst = []
        while q:
            node = q.popleft()
            ans_lst.append(node)
            for i in edges[node]:
                chudu[i] -= 1
                if chudu[i] == 0:
                    q.append(i)
        
        ans_lst.sort()
        return ans_lst

s = Solution()
print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))