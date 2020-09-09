class Solution:
    def findLeastNumOfUniqueInts(self, arr: list, k: int) -> int:
        if k >= len(arr):
            return 0
        
        count_list = []
        visited = set()
        for i in arr:
            if i in visited:
                continue
            count_list.append(arr.count(i))
            visited.add(i)
        
        count_list.sort(reverse=True)
        for i in range(len(count_list)-1, -1, -1):
            if count_list[i] <= k:
                k -= count_list[i]
                count_list.pop()
            else:
                break
        return len(count_list)


sol = Solution()
print(sol.findLeastNumOfUniqueInts([24,119,157,446,251,117,22,168,374,373,323,311,441,213,120,412,200,236,328,24,164,104,331,32,19,223,89,114,152,82,456,381,355,343,157,245,443,368,229,49,82,16,373,142,240,125,8], 
                                41))