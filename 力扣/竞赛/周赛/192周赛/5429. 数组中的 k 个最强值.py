from functools import cmp_to_key
class Solution:
    def getStrongest(self, arr: list, k: int) -> list:
        arr.sort()
        self.m = arr[(len(arr) - 1) // 2]
        def comp(i, j):
            if abs(i-self.m) > abs(j-self.m): return 1
            elif abs(i-self.m) == abs(j-self.m):
                if i > j:
                    return 1
                else:
                    return -1
            else:
                return -1
        ans_lst = list(sorted(arr, key=cmp_to_key(comp), reverse=True))
        return ans_lst[:k]

sol = Solution()
print(sol.getStrongest([6,7,11,7,6,8], 5))