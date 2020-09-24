class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        num_lst = [i for i in range(lo, hi+1)]

        def compare(x: int):
            ans = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3*x + 1
                ans += 1
            return ans
        return sorted(num_lst, key=compare)[k-1]
