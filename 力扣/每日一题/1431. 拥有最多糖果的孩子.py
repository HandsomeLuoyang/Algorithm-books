class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        m = max(candies)
        bl_list = []
        for i in candies:
            if i + extraCandies >= m:
                bl_list.append(True)
            else:
                bl_list.append(False)
        return bl_list