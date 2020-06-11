class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        i, j = 0, n
        ans_lst = []
        for k in range(n):
            ans_lst.append(nums[i])
            ans_lst.append(nums[j])
            i += 1
            j += 1
        return ans_lst