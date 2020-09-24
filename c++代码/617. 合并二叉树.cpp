#include <iostream>
using namespace std;

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
    TreeNode *mergeTrees(TreeNode *t1, TreeNode *t2)
    {
        if (!t1)
            return t2;
        if (!t2)
            return t1;
        t1->val += t2->val;
        this->helper(t1, t2);
        return t1;
    }
    void helper(TreeNode *node1, TreeNode *node2)
    {
        if (!node2->left && !node2->right)
            return;
        if (node1->left && node2->left)
        {
            node1->left->val += node2->left->val;
            this->helper(node1->left, node2->left);
        }
        if (!node1->left && node2->left)
            node1->left = node2->left;
        if (node1->right && node2->right)
        {
            node1->right->val += node2->right->val;
            this->helper(node1->right, node2->right);
        }
        if (!node1->right && node2->right)
            node1->right = node2->right;
    }
};