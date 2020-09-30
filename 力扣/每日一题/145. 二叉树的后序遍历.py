# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        ans_lst = []
        if not root:
            return []
        node_stack = []
        node = root
        while node.left or node.right:
            pass
        