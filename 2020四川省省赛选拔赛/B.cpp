#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 100
#define MAXM 6000
#define eps (1e-8)
#define INF 1000000000
#define abs(x) ((x) > 0 ? (x) : -(x))
#define sqr(x) ((x) * (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

typedef long long LL;

int n, m, MOD;
int beg[MAXN], end[MAXN];
int f[MAXN], g[MAXN][MAXM], s[MAXN][MAXM];

void swap(int &x, int &y)
{
    int temp = x;
    x = y;
    y = temp;
}

int getsum(int x, int d, int u)
{
    return (s[u][x] - s[d - 1][x]) % MOD;
}

int main()
{
    while (scanf("%d", &n) != EOF && n)
    {
        int ans = 0;
        for (int i = 0; i <= n; ++i)
            scanf("%d", &f[i]);
        scanf("%d%d", &m, &MOD);
        bool flag = true;
        for (int i = 0; i < n; ++i)
            if (abs(f[i] - f[i + 1]) == 1)
            {
                int a = f[i], b = f[i + 1];
                for (int j = 2; j <= m; ++j)
                {
                    a = f[a];
                    b = f[b];
                    if (abs(a - b) != 1)
                        break;
                }
                if (a == i && b == i + 1)
                {
                    puts("Infinity");
                    flag = false;
                    break;
                }
            }
        if (!flag)
            continue;
        for (int i = 1; i <= n; ++i)
        {
            beg[i] = MIN(f[i], f[i - 1]);
            end[i] = MAX(f[i], f[i - 1]);
        }
        for (int i = 1; i <= n; ++i)
        {
            for (int j = 1; j <= n; ++j)
                g[j][1] = 0;
            g[i][1] = 1;
            s[0][1] = 0;
            for (int j = 1; j <= n; ++j)
                s[j][1] = (s[j - 1][1] + g[j][1]) % MOD;
            for (int step = 2; step <= m; ++step)
            {
                s[0][step] = 0;
                for (int j = 1; j <= n; ++j)
                {
                    g[j][step] = getsum(step - 1, beg[j] + 1, end[j]);
                    s[j][step] = s[j - 1][step] + g[j][step];
                }
            }
            ans = (ans + getsum(m, beg[i] + 1, end[i])) % MOD;
        }
        for (int i = 0; i <= n; ++i)
        {
            int a, b, c;
            b = f[i];
            if (i > 0)
                a = f[i - 1];
            if (i < n)
                c = f[i + 1];
            for (int j = 2; j <= m; ++j)
            {
                if (i > 0)
                    a = (a < b) ? f[b - 1] : ((a > b) ? f[b + 1] : f[b]);
                if (i < n)
                    c = (c < b) ? f[b - 1] : ((c > b) ? f[b + 1] : f[b]);
                b = f[b];
            }
            if ((i == 0 || a >= i) && b == i && (i == n || c <= i))
                ans = (ans + 1) % MOD;
            else if (i > 0 && i < n && b == i && a < i && c > i)
                ans = (ans - 1) % MOD;
        }
        printf("%d/n", (ans + MOD) % MOD);
    }
    return 0;
}