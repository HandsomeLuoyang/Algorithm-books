class Solution:
    def minCost(self, s: str, cost: list) -> int:
        if len(s) == 1:
            return 0
        ss = list(s)
        repeat_list = []
        cost_cnt = 0
        sep = 0
        i = 1
        while i < len(ss):
            if ss[i] == ss[i-1]:
                start = i-1
                while i < len(ss):
                    if ss[i] == ss[i-1]:
                        sep += 1
                        i += 1
                    else: 
                        repeat_list.append([start, start + sep])
                        sep = 0
                        break
            if sep != 0:
                repeat_list.append([start, start + sep])
            i += 1
        
        for item in repeat_list:
            cost_cnt += sum(sorted(cost[item[0]: item[1]+1])[:-1])
        
        return cost_cnt

s = Solution()
print(s.minCost("abaac", [1, 2, 3, 4, 5]))