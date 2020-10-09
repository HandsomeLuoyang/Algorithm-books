#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;

int cal_weights(int node, vector<int> visited, map<int, int> weight, map<int, vector<int> > edges)
{
    int max_weight = 0;
    max_weight += weight[node];
    visited[node] = 1;
    queue<int> q;
    for (int i = 0;i<edges[node].size();i++)
    {
        if(!visited[edges[node][i]])
        {
            visited[edges[node][i]] = 1;
            max_weight += weight[edges[node][i]];
            q.push(edges[node][i]);
        }
    }
    // for (int i = 1; i < visited.size(); i++)
    // {
    //     if (matrix[node][i] && !visited[i])
    //     {
    //         visited[i] = 1;
    //         max_weight += weight[i];
    //         q.push(i);
    //     }
    // }
    while (!q.empty())
    {
        int new_node = q.front();
        q.pop();
        for (int i = 0; i < edges[new_node].size(); i++)
        {
            if (!visited[edges[new_node][i]])
            {
                visited[edges[new_node][i]] = 1;
                max_weight += weight[edges[new_node][i]];
                q.push(edges[new_node][i]);
            }
        }
    }
    // while (!q.empty())
    // {
    //     int new_node = q.front();
    //     q.pop();
    //     for (int i = 1; i < visited.size(); i++)
    //     {
    //         if (matrix[new_node][i] && !visited[i])
    //         {
    //             visited[i] = 1;
    //             max_weight += weight[i];
    //             q.push(i);
    //         }
    //     }
    // }
    return max_weight;
}

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int n;
        scanf("%d", &n);
        // 矩阵初始化
        // vector<vector<int> > matrix;
        // for (int i = 0; i < n + 1; i++)
        // {
        //     vector<int> tmp_vec(n + 1, 0);
        //     matrix.push_back(tmp_vec);
        // }
        // 改成出度临街表
        map<int, vector<int> > edges;

        // 记录每个节点的权重
        map<int, int> weight;
        for (int i = 1; i < n + 1; i++)
        {
            int tmp;
            scanf("%d", &tmp);
            weight[i] = tmp;
        }
        // 构建临接矩阵
        for (int i = 0; i < n - 1; i++)
        {
            int left_node, right_node;
            scanf("%d %d", &left_node, &right_node);
            // matrix[left_node][right_node] = 1;
            // matrix[right_node][left_node] = 1;
            edges[left_node].push_back(right_node);
            edges[right_node].push_back(left_node);
        }

        // 记录总体最小值
        int all_min = INT32_MAX;

        // 分别以每个节点作为栖息点，向支线延伸
        for (int i = 1; i < n + 1; i++)
        {
            vector<int> visited(n + 1, 0);
            visited[i] = 1;
            // 这个点连接的每一条边的另一个点都是另一棵树，互补相连，直接计算就可以
            // 计算各部分最大值
            int sector_max = 0;

            for (int t = 0;t<edges[i].size();t++)
            {
                int tmp_weight = cal_weights(edges[i][t], visited, weight, edges);
                sector_max = tmp_weight > sector_max ? tmp_weight : sector_max;
                // printf("%d:sector_max:%d----\n", edges[i][t], sector_max);
            }
            // printf("%d---\n", sector_max);

            // for (int t = 1; t < n + 1; t++)
            // {
            //     // 若是相连
            //     if (matrix[i][t])
            //     {
            //         int tmp_weight = cal_weights(t, visited, weight, matrix);
            //         sector_max = tmp_weight > sector_max ? tmp_weight : sector_max;
            //     }
            // }
            // 获取最小值
            all_min = sector_max < all_min ? sector_max : all_min;
        }
        printf("%d\n", all_min);
    }
    return 0;
}