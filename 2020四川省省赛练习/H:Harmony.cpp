#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int x, int y)
{
    int t = x % y;
    while (t != 0)
    {
        x = y;
        y = t;
        t = x % y;
    }
    return y;
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int m, n;
        scanf("%d %d", &m, &n);
        printf("%d\n", gcd(m, n) + m + n);
    }
    return 0;
}