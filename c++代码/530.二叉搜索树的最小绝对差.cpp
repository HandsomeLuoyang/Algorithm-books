#include <iostream>
#include <vector>
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
private:
    vector<int> num_lst;

public:
    int getMinimumDifference(TreeNode *root)
    {
        zhongxu(root);
        int min_num = INT32_MAX;
        for (int i = 0; i < num_lst.size()-1; i++)
        {
            min_num = min_num < abs(num_lst[i] - num_lst[i+1]) ? min_num : abs(num_lst[i] - num_lst[i+1]);
        }
        return min_num;
        
    }
    void zhongxu(TreeNode* root)
    {
        if (root->left) zhongxu(root->left);
        if (root) this->num_lst.push_back(root->val);
        if (root->right) zhongxu(root->right);
    }
};