from typing import *


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        length = len(arr)
        left = int(length * 0.05)
        right = int(length - left)
        arr.sort()
        return sum(arr[left:right]) / len(arr[left:right])
