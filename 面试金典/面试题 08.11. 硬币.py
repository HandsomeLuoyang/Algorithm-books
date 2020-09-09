class Solution:
    def waysToChange(self, n: int) -> int:
        self.ans = 0
        self.set = set()
        self.digui(n, [-1, ])
        return len(self.set)
    
    def digui(self, score:int, lst:list):
        print(score)
        if score < 5:
            self.set.add(lst[:])
        elif 5 <= score <10:
            self.digui(score - 5, lst[:])
            self.digui(score - 1, lst[:].append(1))
        elif 10 <= score < 25:
            self.digui(score - 10, lst[:].append(10))
            self.digui(score - 5, lst[:].append(5))
            self.digui(score - 1, lst[:].append(1))
        else:
            self.digui(score - 25, lst[:].append(25))
            self.digui(score - 10, lst[:].append(10))
            self.digui(score - 5, lst[:].append(5))
            self.digui(score - 1, lst[:].append(1))

s = Solution()
s.waysToChange(10)