#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int m, n, i, j, flag1, flag2;
    double w, x[1005], y[1005];
    while (cin >> m >> n >> w, (m + n + w))
    {
        memset(x, 0, sizeof(x));
        memset(y, 0, sizeof(y));
        flag1 = 1;
        flag2 = 1;
        for (i = 0; i < m; i++)
        {
            scanf("%lf", &x[i]);
        }
        for (j = 0; j < n; j++)
        {
            scanf("%lf", &y[j]);
        }
        sort(x, x + m);
        sort(y, y + n);
        if (x[0] > 1.0 * w / 2 || 75 - x[m - 1] > 1.0 * w / 2)
            flag1 = 0;
        for (i = 1; i < m; i++)
        {
            if (x[i] - x[i - 1] > w)
            {
                flag1 = 0;
                break;
            }
        }
        if (y[0] > 1.0 * w / 2 || 100 - y[n - 1] > 1.0 * w / 2)
            flag2 = 0;
        for (j = 1; j < n; j++)
        {
            if (y[j] - y[j - 1] > w)
            {
                flag2 = 0;
                break;
            }
        }
        if (flag1 && flag2)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}