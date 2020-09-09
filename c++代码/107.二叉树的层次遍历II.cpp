#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
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
    vector<vector<int>> levelOrderBottom(TreeNode *root)
    {
        if (!root)
        {
            return v;
        }
        q.push(root);
        this->helper(q);
        reverse(v.begin(), v.end());
        return v;
    }

    void helper(queue<TreeNode *> q)
    {
        if (q.empty()) return;
        vector<int> tmp_v;
        queue<TreeNode *> new_q;
        while (!q.empty())
        {
            TreeNode *node = q.front();
            q.pop();
            tmp_v.push_back(node->val);
            if (node->left)
                new_q.push(node->left);
            if (node->right)
                new_q.push(node->right);
        }
        v.push_back(tmp_v);
        this->helper(new_q);
    }
    queue<TreeNode *> q;
    vector<vector<int>> v;
};
