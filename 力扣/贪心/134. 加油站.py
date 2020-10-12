from typing import *

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cha_list = [0] * len(gas)
        for i in range(len(gas)):
            cha_list[i] = gas[i] - cost[i]
        if sum(cha_list) < 0:
            return -1

        def helper(begin:int):
            if gas[begin] < cost[begin]:
                return -1
            now_gas = 0
            old_begin = begin
            for i in range(len(gas)):
                now_gas += gas[begin]
                now_gas -= cost[begin]
                begin = (begin + 1) % len(gas)
                if now_gas < 0:
                    return -1
            return old_begin
        for begin in range(len(gas)):
            ans = helper(begin)
            if ans != -1:
                return ans
        return -1

