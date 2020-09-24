import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> list:
        if not root:
            return []
        dct = collections.defaultdict(int)
        def helper(root):
            if not root:
                return 
            dct[root.val] += 1
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
        helper(root)
        tmp_lst = sorted(dct.items(), key=lambda x:x[1], reverse=True)
        max_apper = tmp_lst[0][1]
        ans_lst = [tmp_lst[0][0]]
        for i in range(1, len(tmp_lst)):
            if tmp_lst[i][1] == max_apper:
                ans_lst.append(tmp_lst[i][0])
        return ans_lst