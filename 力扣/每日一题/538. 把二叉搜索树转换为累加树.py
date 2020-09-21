# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        bn = None
        def helper(node):
            nonlocal bn
            if node.right:
                helper(node.right)
            if bn:
                node.val += bn.val
            bn = node
            if node.left:
                helper(node.left)
            return node.val
        if root:
            helper(root)
        return root
