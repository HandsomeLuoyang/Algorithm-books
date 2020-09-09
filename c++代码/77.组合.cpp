#include <iostream>
#include <vector>
#include <deque>
using namespace std;

class Solution
{
public:
    vector<vector<int>> combine(int n, int k)
    {
        this->helper(1, this->tmp_vec, n, k);
        return this->res;
    }

    void helper(int start, vector<int> tmp_v, int n, int k)
    {
        if (tmp_v.size() == k)
        {
            this->res.push_back(tmp_v);
            return ;
        }
        for (int i = start; i < n+1; i++)
        {
            tmp_v.push_back(i);
            this->helper(i + 1, tmp_v, n, k);
            tmp_v.pop_back();
        }
    }
    vector<vector<int> > res;
    vector<int> tmp_vec;
};

int main()
{
    Solution s;
    s.combine(4, 2);
    return 0;
}