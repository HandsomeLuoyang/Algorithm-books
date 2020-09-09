#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

bool cmp(const pair<int, int> &p1, const pair<int, int> &p2) //要用常数，不然编译错误
{
    return p1.second > p2.second;
}
class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        map<int, int> mmp;
        for (auto i : nums)
        {
            if (mmp.count(i) == 0)
            {
                mmp.insert(pair<int, int>{i, 1});
            }
            else
            {
                mmp[i] += 1;
            }
        }
        vector<pair<int, int>> arr;
        for (map<int, int>::iterator it = mmp.begin(); it != mmp.end(); ++it)
        {
            arr.push_back(make_pair(it->first, it->second));
        }
        sort(arr.begin(), arr.end(), cmp);

        vector<int> v;
        for (int i = 0; i < k; i++)
        {
            v.push_back(arr.at(i).first);
        }

        return v;
    }
};

int main()
{
    vector<int> v{1, 2, 3, 4, 5};
    Solution s;
    s.topKFrequent(v, 3);
    return 0;
}