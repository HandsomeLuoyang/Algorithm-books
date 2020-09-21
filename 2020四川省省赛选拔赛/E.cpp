#include <iostream>
#include <vector>
#include <string>
#include <stack>
#define N 40001
using namespace std;

char s[] = "AGTC";
vector<int> g[N];
stack<int> sta;

int dfn[N], low[N], belong[N], a[10001];
int n, t, dindex, cnt;
char ch, v[N], nxt[256];
string str;

inline int dist(char a, char b)
{
    int x = strchr(s, a) - s, y = strchr(s, b) - s, d = abs(x - y);
    return min(d, 4 - d);
}

inline void add_or(int x, int v1, int y, int v2)
{
    g[(x * 2) | (v1 ^ 1)].push_back((y * 2) | v2);
    g[(y * 2) | (v2 ^ 1)].push_back((x * 2) | v1);
}

inline void add_equal(int x, int y)
{
    add_or(x, 1, y, 0);
    add_or(x, 0, y, 1);
}

inline void add_distinct(int x, int y)
{
    add_or(x, 0, y, 0);
    add_or(x, 1, y, 1);
}

inline void sets(int x, int val)
{
    int y = (x * 2) | val;
    g[y ^ 1].push_back(y);
}

inline void tarjan(int x)
{
    low[x] = dfn[x] = ++dindex;
    v[x] = true;
    sta.push(x);
    for (int i = 0; i < g[x].size(); i++)
    {
        int y = g[x][i];
        if (!dfn[y])
        {
            tarjan(y);
            low[x] = min(low[x], low[y]);
        }
        else if (v[y])
            low[x] = min(low[x], dfn[y]);
    }
    if (dfn[x] == low[x])
    {
        cnt++;
        int j = 0;
        do
        {
            j = sta.top();
            sta.pop();
            v[j] = 0;
            belong[j] = cnt;
        } while (j != x);
    }
}

int main()
{
    for (int i = 0; i < 4; i++)
        nxt[s[i]] = s[(i + 1) % 4];
    while (~scanf("%d%d", &n, &t) && (t || n))
    {
        getchar();
        getline(cin, str);
        for (int i = 0; i < n * 4; i++)
        {
            dfn[i] = low[i] = belong[i] = 0;
            v[i] = 0;
            g[i].clear();
        }
        for (int i = 0; i < n - 1; i++)
            add_or(i, 0, i + 1, 0);
        while (t--)
        {
            int l;
            scanf("%d%c", &l, &ch);
            for (int i = 1; i <= l; i++)
                scanf("%d", &a[i]);
            for (int i = 1, j = l; i < j; i++, j--)
            {
                int x = a[i], y = a[j], d = dist(str[x], str[y]);
                if (d == 0)
                {
                    add_equal(x, y);
                    add_equal(x + n, y + n);
                }
                else if (d == 1)
                {
                    add_distinct(x, y);
                    bool rev = (str[y] != nxt[str[x]]);
                    add_or(x, 1, y + n, rev);
                    add_or(y, 1, x + n, rev ^ 1);
                }
                else
                {
                    sets(x, 1);
                    sets(y, 1);
                    add_distinct(x + n, y + n);
                }
            }
        }
        int flag = 1;
        cnt = dindex = 0;
        for (int i = 0; i < n * 4; i++)
            if (!dfn[i])
                tarjan(i);
        for (int i = 0; flag && i < n * 2; i += 2)
            if (belong[i] == belong[i + 1])
                flag = 0;
        puts(flag ? "YES" : "NO");
    }
    return 0;
}