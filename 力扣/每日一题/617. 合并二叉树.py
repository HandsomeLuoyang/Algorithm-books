# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        def helper(node1, node2):
            if not node2.left and not node2.right:
                return 
            if node1.left and node2.left:
                node1.left.val += node2.left.val
                helper(node1.left, node2.left)
            if not node1.left and node2.left:
                node1.left = node2.left
            if node1.right and node2.right:
                node1.right.val += node2.right.val
                helper(node1.right, node2.right)
            if not node1.right and node2.right:
                node1.right = node2.right
        helper(t1, t2)
        return t1