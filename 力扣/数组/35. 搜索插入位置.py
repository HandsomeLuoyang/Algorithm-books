class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if target > nums[-1]:
            return length
        if target < nums[0]:
            return 0
        lo, hi = 0, length - 1
        mid = (lo + hi) // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        return mid if nums[mid] > target else mid + 1

s = Solution()
print(s.searchInsert([1,3,5,6], 2))