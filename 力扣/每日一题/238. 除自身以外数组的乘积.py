class Solution:
    def productExceptSelf(self, nums: list) -> list:
        # ans_list = [0 for _ in range(len(nums))]
        # if nums.count(0) >= 2:
        #     return ans_list
        # tmp_prod = 1
        # for i in range(len(nums)):
        #     tmp_prod *= nums[i]
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         ans_list[i] = tmp_prod // nums[i]
        #     else:
        #         tt_prod = 1
        #         for j in range(len(nums)):
        #             if j != i:
        #                 tt_prod *= nums[j]
        #         ans_list[i] = tt_prod
        # return ans_list

        ans = [0] * len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        R = 1
        for i in reversed(range(len(nums))):
            ans[i] = ans[i] * R
            R *= nums[i]
        return an1367. 二叉树中的列表s
