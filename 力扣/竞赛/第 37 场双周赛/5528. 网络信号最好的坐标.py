from typing import *
import math


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_x = -1
        max_y = -1
        for i in towers:
            max_x = max_x if max_x > i[0] else i[0]
            max_y = max_y if max_y > i[1] else i[1]

        max_x = max_x + radius
        max_y = max_y + radius

        max_xinhao = 0
        ans_x = ans_y = -1
        for i in range(max_x+1):
            for j in range(max_y + 1):
                score = 0
                for item in towers:
                    distance = math.sqrt((item[0] - i) ** 2 + (item[1] - j) ** 2)
                    if distance <= radius:
                        score += int(item[2] / (1 + distance))
                if max_xinhao < score:
                    max_xinhao = score
                    ans_x, ans_y = i, j
        return [ans_x, ans_y]