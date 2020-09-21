#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <cstring>
#include <vector>
using namespace std;
const int maxn = 355;
const int inf = 1e8;
int n, m, size, minw, ans;
int fa[maxn];
bool vis[maxn];
int w[maxn][maxn];

//int find(int x) { return x==fa[x] ? x : find(fa[x]); }
struct Edge
{
    int u, v, w;
    Edge(int uu, int vv, int ww) : u(uu), v(vv), w(ww) {}
    Edge() {}
    bool operator<(const Edge &e) const { return w < e.w; }
} edge[maxn * maxn / 2];

int CA(int u, int v)
{
    memset(vis, 0, sizeof(vis));
    int x = u;
    while (!vis[x])
    {
        vis[x] = true;
        if (x == fa[x])
            break;
        x = fa[x];
    }
    x = v;
    while (!vis[x] && fa[x] != x)
        x = fa[x];
    if (vis[x])
        return x;
    else
        return -1;
}

void findremove(const Edge &e)
{
    int rt = CA(e.u, e.v);
    if (rt == -1)
        return;
    Edge minedge;
    minedge.w = inf;
    int y = e.u;
    int x = fa[y];
    while (x != y && y != rt)
    {
        if (w[x][y] < minedge.w)
            minedge = Edge(x, y, w[x][y]);
        y = x;
        x = fa[x];
    }
    y = e.v;
    x = fa[y];
    while (y != rt && x != y)
    {
        if (w[x][y] < minedge.w)
            minedge = Edge(x, y, w[x][y]);
        y = x;
        x = fa[x];
    }

    fa[minedge.v] = minedge.v;
    minw = inf;
    for (int i = 0; i < n; ++i)
        if (fa[i] != i && minw > w[fa[i]][i])
            minw = w[fa[i]][i];
    --size;
}

void addedge(const Edge &e)
{
    if (fa[e.u] == e.u)
        fa[e.u] = e.v;
    else if (fa[e.v] == e.v)
        fa[e.v] = e.u;
    else
    {
        vector<int> v;
        int x = e.u;
        while (true)
        {
            v.push_back(x);
            if (x == fa[x])
                break;
            x = fa[x];
        }
        for (int i = v.size() - 1; i > 0; --i)
            fa[v[i]] = v[i - 1];
        fa[e.u] = e.v;
    }
    minw = min(minw, e.w);
    ++size;
}

void input()
{
    scanf("%d", &m);
    int u, v, w;
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d%d", &u, &v, &w);
        edge[i] = Edge(u, v, w);
        ::w[u][v] = ::w[v][u] = w;
    }
}

void solve()
{
    size = 0;
    sort(edge, edge + m);
    for (int i = 0; i < n; ++i)
        fa[i] = i;
    ans = minw = inf;
    for (int i = 0; i < m; ++i)
    {
        findremove(edge[i]);
        addedge(edge[i]);
        if (size == n - 1)
            ans = min(ans, edge[i].w - minw);
    }
    printf("%d\n", ans);
}

int main()
{
    //	freopen("input.in","r",stdin);
    while (scanf("%d", &n) == 1, n)
    {
        input();
        solve();
    }
    return 0;
}