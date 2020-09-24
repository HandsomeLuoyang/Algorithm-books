#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;

class Solution
{
private:
    vector<vector<int>> edges;
    vector<int> indeg;

public:
    vector<int> canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        edges.resize(numCourses);
        indeg.resize(numCourses);
        for (const auto &info : prerequisites)
        {
            edges[info[1]].push_back(info[0]);
            indeg[info[0]]++;
        }
        queue<int> q;
        for (int i = 0; i < numCourses; i++)
        {
            if (indeg[i] == 0)
                q.push(i);
        }
        vector<int> visited;
        while (!q.empty())
        {
            int u = q.front();
            q.pop();
            visited.push_back(u);
            for (auto v : edges[u])
            {
                --indeg[v];
                if (indeg[v] == 0)
                    q.push(v);
            }
        }
        if (visited.size() == numCourses)
            return visited;
        else
        {
            vector<int> v;
            return v;
        }
    }
};

int main()
{
    Solution s;
    return 0;
}