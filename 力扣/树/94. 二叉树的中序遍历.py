# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归版本
    # def inorderTraversal(self, root: TreeNode) -> list:
    #     self.tree_list = []
    #     self.inorderTravers(root)
    #     return self.tree_list
    
    # def inorderTravers(self, root):
    #     if root is None:
    #         return 
    #     self.inorderTravers(root.left)
    #     self.tree_list.append(root.val)
    #     self.inorderTravers(root.right)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        self.stack = []
        self.ans_lst = []
        while root or self.stack:
            while root:
                self.stack.append(root)
                root =  root.left
            
            root = self.stack.pop()
            self.ans_lst.append(root.val)
            root = root.right
        return self.ans_lst