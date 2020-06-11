# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        self.length = len(nums)
        if not nums:
            return 
        if self.length == 1:
            return TreeNode(nums[0])
        self.nums = nums
        mid = self.length // 2
        root = TreeNode(nums[mid])
        # 区间分治
        root.left = self.helper(0, mid-1)
        root.right = self.helper(mid + 1, self.length - 1)
        return root


    def helper(self, l, r):
        if r == l:
            return TreeNode(self.nums[l])
        if r < l:
            return 
        mid = l + (r - l) // 2
        root = TreeNode(self.nums[mid])
        root.left = self.helper(l, mid-1)
        root.right = self.helper(mid+1, r)
        return root


sol = Solution()
sol.sortedArrayToBST([-10,-3,0,5,9])