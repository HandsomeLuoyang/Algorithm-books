class Solution:
    def combine(self, n: int, k: int):
        res_lst = []
        def helper(start, path:list):
            path = path[:]
            if len(path) == k:
                res_lst.append(path)
                return
            for i in range(start, n+1):
                path.append(i)
                helper(i+1, path)
                path.pop()
        path = []
        helper(1, path)
        return res_lst

s = Solution()
s.combine(4, 2)