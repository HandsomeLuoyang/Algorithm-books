struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
public:
    TreeNode *invertTree(TreeNode *root)
    {
        if (!root)
            return NULL;
        helper(root);
        return root;
    }

    void helper(TreeNode *root)
    {
        if (root->left)
            helper(root->left);
        if (root->right)
            helper(root->right);
        TreeNode *tmp = root->left;
        root->left = root->right;
        root->right = tmp;
    }
};