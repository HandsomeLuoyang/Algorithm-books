from typing import *
from collections import defaultdict
class Solution:
    """代码超时了"""
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        dict_edges = defaultdict(list)
        for item in edges:
            dict_edges[item[0]].append(item[1])
            dict_edges[item[1]].append(item[0])
        ans_lst = [0] * n

        def helper(node:int, visited:List[int]):
            max_height = 1
            for i in dict_edges[node]:
                if visited[i]:
                    continue
                visited[i] = 1
                tmp_height = 1 + helper(i, visited)
                max_height = max_height if max_height > tmp_height else tmp_height
            return max_height
        
        for i in range(n):
            visited = [0] * n
            visited[i] = 1
            ans_lst[i] = helper(i, visited)
        min_height = min(ans_lst)
        return [i for i in range(len(ans_lst)) if ans_lst[i] == min_height]

s = Solution()
s.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])