class Solution:
    def breakfastNumber(self, staple: list, drinks: list, x: int) -> int:
        staple.sort()
        drinks.sort()
        print(staple, drinks)

        max_i = 0
        max_j = 0

        for i in range(len(staple)):
            for j in range(len(drinks)):
                if staple[i] + drinks[j] > x:
                    break
                if i > max_i:
                    max_i = i
                if j > max_j:
                    max_j = j


        return ((max_i+1) * (max_j+1)) % (1000000007)


s = Solution()
print(s.breakfastNumber([2,1,1], [8,9,5,1], 9))
