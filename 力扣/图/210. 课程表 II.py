import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:
        edge = collections.defaultdict(list)
        visited = []
        indeg = [0] * numCourses
        for item in prerequisites:
            edge[item[1]].append(item[0])
            indeg[item[0]] += 1
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            u = q.popleft()
            visited.append(u)
            for v in edge[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        return visited if len(visited) == numCourses else []