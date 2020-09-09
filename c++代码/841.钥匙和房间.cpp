#include <iostream>
#include <vector>
#include <set>
using namespace std;

class Solution
{
public:
    set<int> ans_set;

    bool canVisitAllRooms(vector<vector<int>> &rooms)
    {
        int length = rooms.size();
        if (length < 1)
            return true;
        this->dfs(0, rooms);
        if (this->ans_set.size() == length)
            return true;
        else
            return false;
    }
    void dfs(int n, vector<vector<int>> &rooms)
    {
        if (this->ans_set.count(n) == 1)
            return;
        this->ans_set.insert(n);
        for (int i = 0; i < rooms[n].size(); i++)
        {
            this->dfs(rooms[n][i], rooms);
        }
    }
};

int main()
{
    return 0;
}