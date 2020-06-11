class Solution:
    def minArray(self, numbers: list) -> int:
        for i in range(len(numbers)-1):
            if numbers[i+1] < numbers[i]:
                return numbers[i+1]
        return numbers[0]
        # return min(numbers)
