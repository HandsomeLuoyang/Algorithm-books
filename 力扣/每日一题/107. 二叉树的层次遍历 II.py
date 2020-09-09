# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        ans_lst = []
        dq = []
        dq.append(root)
        def helper(dq:list):
            if len(dq) == 0:
                return 
            new_dq = []
            tmp_lst = []
            while len(dq) > 0:
                node = dq.pop(0)
                tmp_lst.append(node.val)
                if node.left:
                    new_dq.append(node.left)
                if node.right:
                    new_dq.append(node.right)
            ans_lst.append(tmp_lst)
            helper(new_dq)
        helper(dq)
        return ans_lst[::-1]

