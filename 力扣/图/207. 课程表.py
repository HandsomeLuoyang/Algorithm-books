import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        # 拓扑排序
        dct = collections.defaultdict(list)
        visited = 0
        indeg = [0] * numCourses

        for item in prerequisites:
            dct[item[1]].append(item[0])
            indeg[item[0]] += 1
        
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            visited += 1
            u = q.popleft()
            for v in dct[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses