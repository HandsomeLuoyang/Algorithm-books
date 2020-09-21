#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
int cost[128][128], sz, dp[210][210][26], n, m, len;
char sym[26], ch[128][128], str[210];
bool first;

int main()
{
    ios_base::sync_with_stdio(false);
    while (cin >> n && n)
    {
        if (first)
            cout << endl;
        else
            first = true;

        for (int i = 0; i < n; ++i)
            cin >> sym[i];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                cin >> cost[sym[i]][sym[j]] >> ch[sym[i]][sym[j]] >> ch[sym[i]][sym[j]];

        cin >> m;
        while (m--)
        {
            memset(dp, -1, sizeof dp);
            cin >> str;
            len = strlen(str);
            for (int i = 0; i < len; ++i)
                dp[i][i][str[i]] = 0;
            for (int length = 2; length <= len; ++length)
                for (int i = 0, j = length - 1; j < len; ++i, ++j)
                    for (int k = i; k < j; ++k)
                        for (int le = 0; le < n; ++le)
                            if (dp[i][k][sym[le]] != -1)
                                for (int ri = 0; ri < n; ++ri)
                                    if (dp[k + 1][j][sym[ri]] != -1)
                                        if (dp[i][j][ch[sym[le]][sym[ri]]] == -1 || dp[i][j][ch[sym[le]][sym[ri]]] > dp[i][k][sym[le]] + dp[k + 1][j][sym[ri]] + cost[sym[le]][sym[ri]])
                                            dp[i][j][ch[sym[le]][sym[ri]]] = dp[i][k][sym[le]] + dp[k + 1][j][sym[ri]] + cost[sym[le]][sym[ri]];

            int ans = -1;
            for (int i = 0; i < n; ++i)
                if (dp[0][len - 1][sym[i]] != -1)
                    ans = (ans == -1 ? i : (dp[0][len - 1][sym[i]] < dp[0][len - 1][sym[ans]] ? i : ans));
            cout << dp[0][len - 1][sym[ans]] << '-' << sym[ans] << endl;
        }
    }
    return 0;
}