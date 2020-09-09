# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        """
        对二叉树每个节点执行搜索函数
        """
        if not root:
            return False
        if self.helper(root, head):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def helper(self, tree_root, list_root):
        """
        递归搜索函数，从根结点向左右不断搜索
        """
        if not list_root:
            return True
        if not tree_root or tree_root.val != list_root.val:
            return False
        return self.helper(tree_root.left, list_root.next) or self.helper(tree_root.right, list_root.next)