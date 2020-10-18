# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        num_lst = []
        def zhongxu(root:TreeNode):
            if root.left:
                zhongxu(root.left)
            num_lst.append(root.val)
            if root.right:
                zhongxu(root.right)

        zhongxu(root)
        min_num = float('INF')
        for i in range(len(num_lst) -1):
            min_num = min_num if min_num < abs(num_lst[i] - num_lst[i+1]) else abs(num_lst[i] - num_lst[i+1])
        return min_num