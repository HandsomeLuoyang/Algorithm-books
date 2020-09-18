# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        def helper(root):
            if root.left: helper(root.left)
            if root.right: helper(root.right)
            tmp = root.left
            root.left = root.right
            root.right = tmp
        helper(root)
        return root
