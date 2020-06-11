import time


class Solution:
    """我的垃圾解法"""

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = - n
        elif n == 0:
            return 1
        if n == 1:
            return x

        final_ans = 1
        val_dict = {}

        while n >= 2:
            ans = x
            mi = 2
            while mi <= n:
                ans *= ans
                val_dict[mi] = ans
                mi *= 2

            final_ans *= ans
            n = n - mi // 2

            if n == 1:
                final_ans *= x
                break


        return final_ans

class Solution1:
    """大佬1的解法"""
    def myPow(self, x: float, n: int) -> float:
        if x == 0: 
            return 0
        res = 1
        if n < 0: 
            x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

class Solution2:
    """大佬2的解法"""
    def myPow(self, x: float, n: int) -> float:
        if n ==0 : return 1
        if  n>0 :return self.helper(x,n)
        else: return 1/self.helper(x,-n)
        
    def helper(self,x,n):
        if n==1: return x
        
        if n%2 ==0:
            return self.helper(x*x,n/2)
        else:
            return self.helper(x*x,n//2) *x


s1 = Solution1()
s = Solution()
s2 = Solution2()
import time 

n = 14
x = 1111222

st = time.process_time()
s1.myPow(n, x)
ed = time.process_time()
print('大佬1解法时间: {}'.format(ed - st))

st = time.process_time()
s2.myPow(n, x)
ed = time.process_time()
print('大佬2解法时间: {}'.format(ed - st))

st = time.process_time()
s.myPow(n, x)
ed = time.process_time()
print('我的垃圾解法时间: {}'.format(ed - st))