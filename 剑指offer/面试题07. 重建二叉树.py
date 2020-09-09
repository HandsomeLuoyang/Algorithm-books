class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if len(preorder) == 0:
            return
        self.lst = preorder[:]
        # 因为中序遍历需要经常查找值的序号，所以直接用hash的方法记录，提高之后的查询效率
        self.val_dic = {}
        for index, val in enumerate(inorder):
            self.val_dic[val] = index
        # 直接递归
        return self.digui(0, 0, len(inorder) - 1)

    def digui(self, pre_root, in_left, in_right):
        """
        pre_root,根结点在前序列表中的序号
        in_left,中序列表中左子树的开始序号
        in_right,中序列表中右字树的开始序号
        """
        # 终止条件
        if in_left > in_right:
            return
        # 构造节点
        root = TreeNode(self.lst[pre_root])
        # 从中序列表中，找到根结点所在位置，将中序列表分成左右子树
        i = self.val_dic[self.lst[pre_root]]
        # 递归之——递, 分别构造左右子树
        root.left = self.digui(pre_root+1, in_left, i-1)
        root.right = self.digui(i-in_left+pre_root+1, i+1, in_right)
        # 递归之——归，返回根结点
        return root
