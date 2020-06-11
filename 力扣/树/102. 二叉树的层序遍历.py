# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        """
        使用BFS广度优先搜索改造成树的层序遍历
        """
        ans_lst = []
        queue = []
        if root:
            queue.append(root)
        while queue:
            tmp = []
            n = len(queue)
            # 利用一个for循环一次性将一层的数据记录到一个临时列表中
            for i in range(n):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans_lst.append(tmp)
        return ans_lst