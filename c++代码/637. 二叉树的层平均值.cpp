#include <iostream>
#include <vector>
#include <queue>
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
    vector<double> averageOfLevels(TreeNode *root)
    {
        if (!root)
        {
            return ans;
        }

        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty())
        {
            int n = q.size();
            double tmp_val = 0;
            for (int i = 0; i < n; i++)
            {
                TreeNode* node = q.front();
                q.pop();
                tmp_val += node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            ans.push_back(tmp_val/n);
        }
        return ans;
    }
    vector<double> ans;
};