class Solution:
    def numOfSubarrays(self, arr: list, k: int, threshold: int) -> int:
        left = 0
        right = k
        target_sum = k * threshold
        sum_num = sum(arr[left:right])
        ans = 0 if sum_num < target_sum else 1

        while right < len(arr):
            sum_num += arr[right] - arr[left]
            left, right = left + 1, right + 1
            if sum_num >= target_sum:
                ans += 1

        return ans

sol = Solution()
print(sol.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))