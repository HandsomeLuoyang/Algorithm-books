#include <cstdio>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
using namespace std;
struct node
{
    int x, y, z;
    node() {}
    node(int X, int Y, int Z)
    {
        x = X;
        y = Y;
        z = Z;
    }
    bool operator==(const node P) const
    {
        return x == P.x && y == P.y && z == P.z;
    }
} p[5];
int Cross(int i, int j, int k)
{
    node v1(p[i].x - p[k].x, p[i].y - p[k].y, p[i].z - p[k].z), v2(p[j].x - p[k].x, p[j].y - p[k].y, p[j].z - p[k].z);
    return (v1.y * v2.z - v1.z * v2.y) + (v1.z * v2.x - v1.x * v2.z) + (v1.x * v2.y - v1.y * v2.x);
}
bool check(int i, int j, int k)
{
    node v1(p[k].x - p[i].x, p[k].y - p[i].y, p[k].z - p[i].z), v2(p[k].x - p[j].x, p[k].y - p[j].y, p[k].z - p[j].z);
    //向量每项必须符号相反(有一个为0，另一个也必须是0)，否则两向量不相反
    if ((v1.x == 0 && v2.x != 0) || (v1.x != 0 && v2.x == 0))
        return 0;
    if ((v1.y == 0 && v2.y != 0) || (v1.y != 0 && v2.y == 0))
        return 0;
    if ((v1.z == 0 && v2.z != 0) || (v1.z != 0 && v2.z == 0))
        return 0;
    if (v1.x * v2.x > 0 || v1.y * v2.y > 0 || v1.z * v2.z > 0)
        return 0;
    //如果A=α*B(α<0),那么A与B共线且方向相反
    if (v1.x == 0 && v1.y == 0 && v1.z == 0)
        return 0;
    if (v1.x != 0 && v1.y != 0 && v1.x * v2.y != v1.y * v2.x)
        return 0;
    if (v1.x != 0 && v1.z != 0 && v1.x * v2.z != v1.z * v2.x)
        return 0;
    if (v1.y != 0 && v1.z != 0 && v1.y * v2.z != v1.z * v2.y)
        return 0;
    return 1;
}
int main()
{
    //freopen("in.txt","r",stdin);
    while (~scanf("%d%d%d", &p[0].x, &p[0].y, &p[0].z), p[0].x || p[0].y || p[0].z)
    {
        for (int i = 1; i < 4; i++)
            scanf("%d%d%d", &p[i].x, &p[i].y, &p[i].z);
        if (p[0] == p[1] && p[1] == p[2])
        { //3个向量相等
            printf("%s\n", p[3] == p[0] ? "YES" : "NO");
            continue;
        }
        int area = abs(Cross(0, 1, 2));
        if (area == 0)
        { //3条向量共面
            if (p[0] == p[1] || p[0] == p[2] || p[1] == p[2])
            {
                bool flag;
                if (p[0] == p[1])
                    flag = check(0, 2, 3);
                else if (p[0] == p[2])
                    flag = check(0, 1, 3);
                else
                    flag = check(1, 2, 3);
                printf("%s\n", flag ? "YES" : "NO");
            }
            else
                printf("%s\n", (check(0, 1, 3) || check(0, 2, 3) || check(1, 2, 3)) ? "YES" : "NO");
        }
        else
        {
            //第四个点必须在三角形内
            //每个向量的可能性必须大于0，3个小三角形面积必须大于0且等于总面积
            int area1 = abs(Cross(0, 1, 3));
            int area2 = abs(Cross(0, 2, 3));
            int area3 = abs(Cross(1, 2, 3));
            if (area1 > 0 && area2 > 0 && area3 > 0 && area == area1 + area2 + area3)
                printf("YES\n");
            else
                printf("NO\n");
        }
    }
    return 0;
}