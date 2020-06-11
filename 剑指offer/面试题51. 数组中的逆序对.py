class Solution:
    def reversePairs(self, nums: list) -> int:
        # 暴力法，超时了
        # ans = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > nums[j]:
        #             ans += 1
        # return ans

        # 用二分插入法维护一个有序数组试试
        ordered_list = [nums[0]]
        for i in range(1, len(nums)):
            target = nums[i]
            lo, hi = 0, len(ordered_list)
            mid = None
            while lo <= hi:
                mid = (lo + hi) // 2
                if target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            ordered_list.insert