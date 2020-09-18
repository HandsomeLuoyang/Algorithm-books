# Definition for a binary tree node.]
import queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list:
        if not root:
            return []
        q = queue.Queue()
        ans_lst = []
        q.put(root)
        while not q.empty():
            n = q.qsize()
            tmp_val = 0
            for i in range(n):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                tmp_val += node.val
            ans_lst.append(tmp_val/n)
        return ans_lst