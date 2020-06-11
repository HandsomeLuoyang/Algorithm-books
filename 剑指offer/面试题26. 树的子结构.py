# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        # 从树的root节点开始，对每个节点采用深搜
        return self.helper(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
    
    def helper(self, A, B):
        """
        深搜函数
        """
        if not B:
            return True
        if not A:
            return False
        if B.val == A.val:
            return self.helper(A.left, B.left) and self.helper(A.right, B.right)
        else:
            return False