#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

const int MAXN = 101;
const int MAXV = 0x3F3F3F3F;
int dp[MAXN][1 << 6][6];
int a[MAXN];

int main()
{
    int n, m;
    while (scanf("%d%d", &n, &m) != EOF && (n || m))
    {
        for (int i = 1; i <= n; i++)
        {
            scanf("%d", &a[i]);
            a[i]--;
        }
        memset(dp, 63, sizeof(dp));
        for (int i = 0; i < m; i++)
        {
            dp[1][1 << i][i] = (a[1] != i);
        }
        for (int i = 2; i <= n; i++)
        {
            for (int j = 0; j < 1 << m; j++)
            {
                for (int k = 0; k < m; k++)
                {
                    if ((j & (1 << k)) == 0)
                        continue;
                    //if (dp[i-1][j][k] != MAXV)
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k] + (a[i] != k));
                    for (int l = 0; l < m; l++)
                    {
                        if (l == k || (j & (1 << l)) == 0)
                            continue;
                        //if (dp[i-1][j&~(1<<k)][l] != MAXV)
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j & ~(1 << k)][l] + (a[i] != k));
                    }
                }
            }
        }
        int ans = 1 << 30;
        for (int j = 0; j < 1 << m; j++)
        {
            for (int k = 0; k < m; k++)
            {
                if (dp[n][j][k] < ans)
                {
                    ans = dp[n][j][k];
                }
            }
        }
        printf("%d\n", ans);
    }
}