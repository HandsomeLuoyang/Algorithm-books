#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>> &edges)
    {
        vector<int> bian(n);
        for (int i=0;i<edges.size();i++)
        {
            bian[edges[i][1]] ++;
        }
        vector<int> ans;
        for (int i = 0;i<bian.size();i++)
        {
            if (bian[i] == 0) ans.push_back(i);
        }
        return ans;
    }
};