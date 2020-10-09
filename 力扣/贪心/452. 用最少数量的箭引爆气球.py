from typing import *
from collections import deque

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        sorted_points = deque(sorted(points, key=lambda x:x[1]))
        ans = 0
        right = sorted_points[0][0] - 1
        while sorted_points:
            tup = sorted_points.popleft()
            if right < tup[0]:
                ans += 1
                right = tup[1]
            
        return ans
            

s = Solution()
print(s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))