class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_list = [1134903170, 701408733, 433494437, 267914296, 165580141, 102334155, 63245986, 39088169, 24157817, 14930352, 9227465, 5702887, 3524578, 2178309, 1346269,
                    832040, 514229, 317811, 196418, 121393, 75025, 46368, 28657, 17711, 10946, 6765, 4181, 2584, 1597, 987, 610, 377, 233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]
        cnt = 0
        for num in fib_list:
            if k >= num:
                cnt += 1
                k -= num
        return cnt


sol = Solution()
print(sol.findMinFibonacciNumbers(32))
