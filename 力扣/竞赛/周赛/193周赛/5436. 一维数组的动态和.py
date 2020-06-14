class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans_lst = []
        tmp_sum = 0
        for i in nums:
            tmp_sum += i
            ans_lst.append(tmp_sum)
        return ans_lst