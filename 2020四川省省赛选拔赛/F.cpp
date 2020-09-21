#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

deque<int> que, ans;

int num[1 << 21], fa[1 << 21];
int n, m, nxt[21];
bool v[1 << 21];

int main()
{
    while (~scanf("%d%d", &n, &m) && n)
    {
        bool flag = 0;
        int l = 1 << n;
        for (int i = 0; i < l; i++)
            v[i] = fa[i] = 0;
        memset(nxt, 0, sizeof(nxt));
        for (int i = 1; i <= m; i++)
        {
            int u, v;
            scanf("%d%d", &u, &v);
            nxt[u] |= (1 << v);
            nxt[v] |= (1 << u);
        }
        if (m > n - 1)
        {
            puts("Impossible");
            continue;
        }
        v[(1 << n) - 1] = 1;
        que.clear();
        que.push_back((1 << n) - 1);
        while (!que.empty() && !flag)
        {
            int cur = que.front();
            que.pop_front();
            for (int i = 0; i < n; i++)
            {
                int next = 0;
                if (cur & (1 << i))
                {
                    for (int j = 0; j < n; j++)
                        if ((cur & (1 << j)) && j != i)
                            next |= nxt[j];
                    if (!v[next])
                    {
                        v[next] = 1;
                        num[next] = i;
                        fa[next] = cur;
                        que.push_back(next);
                        if (!next)
                        {
                            flag = 1;
                            break;
                        }
                    }
                }
            }
        }
        if (flag)
        {
            ans.clear();
            for (int cur = 0; fa[cur]; cur = fa[cur])
                ans.push_back(num[cur]);
            printf("%d: ", ans.size());
            for (int i = ans.size() - 1; i >= 0; i--)
                printf("%d%c", ans[i], !i ? '\n' : ' ');
        }
        else
            puts("Impossible");
    }
    return 0;
}