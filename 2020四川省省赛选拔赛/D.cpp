// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <string>
#define MAX_V 200

using namespace std;

int n, m;

namespace Tu
{
    struct Edge
    {
        int dest, cap;
        Edge *next, *pair;
        Edge() {}
        Edge(int _dest, int _cap, Edge *_next) : dest(_dest), cap(_cap), next(_next) {}
    };

    Edge *e[MAX_V], *c[MAX_V], *p[MAX_V];
    int Stack[MAX_V], Queue[MAX_V], dist[MAX_V];
    int s, t, maxflow, top;

    inline void clear()
    {
        memset(e, 0, sizeof(e));
    }

    inline void addedge(int a, int b, int c)
    {
        e[a] = new Edge(b, c, e[a]);
        e[b] = new Edge(a, 0, e[b]);
        e[a]->pair = e[b], e[b]->pair = e[a];
    }

    inline bool lab()
    {
        memset(dist, 0x3f, sizeof(dist));
        dist[s] = 0;
        Queue[1] = s;
        for (int l = 1, r = 1; l <= r; l++)
        {
            int i = Queue[l];
            for (Edge *j = e[i]; j; j = j->next)
                if (j->cap && dist[j->dest] > dist[i] + 1)
                {
                    dist[j->dest] = dist[i] + 1;
                    if (j->dest == t)
                        return 1;
                    Queue[++r] = j->dest;
                }
        }
        return 0;
    }

    inline void aug()
    {
        int top = 0;
        Stack[++top] = s;
        memcpy(c, e, sizeof(e));
        while (top)
        {
            int i = Stack[top];
            if (i != t)
            {
                Edge *j;
                for (j = c[i]; j; j = j->next)
                    if (j->cap && dist[j->dest] == dist[i] + 1)
                        break;
                if (j)
                    top++, Stack[top] = j->dest, c[i] = p[top] = j;
                else
                    top--, dist[i] = 1e9;
            }
            else
            {
                int delta = 1e9;
                for (int i = top; i >= 2; i--)
                    delta = std::min(delta, p[i]->cap);
                maxflow += delta;
                for (int i = top; i >= 2; i--)
                {
                    p[i]->cap -= delta, p[i]->pair->cap += delta;
                    if (!p[i]->cap)
                        top = i - 1;
                }
            }
        }
    }

    inline int dinic()
    {
        maxflow = 0;
        while (lab())
            aug();
        return maxflow;
    }

    inline void BuildAnswer()
    {
        for (int i = 1; i <= n; i++)
        {
            for (Edge *j = e[i]; j; j = j->next)
            {
                if (j->dest == s || j->dest == t)
                    continue; //连向源汇的边当然不用产生答案
                bool flag = (j->cap);
                if (!flag)
                {
                    addedge(s, i, 1);
                    addedge(j->dest, t, 1);
                    j->cap = j->pair->cap = 0; //尝试封死这条边
                    dinic();                   //看是否能找到增广路
                    if (maxflow <= 0)
                        e[s]->cap = e[j->dest]->cap = 0; //找不到则封死新加的边
                    else
                        flag = 1;
                }
                j->cap = j->pair->cap = 0; //直接封死该边
                if (flag)
                    putchar('N');
                else
                    putchar('Y');
            }
            putchar('\n');
        }
    }
} // namespace Tu

int main()
{
    while (~scanf("%d%d", &n, &m) && n && m)
    {
        int sum1 = 0, sum2 = 0, c;
        Tu::clear();
        int s = Tu::s = 0;
        for (int i = 1; i <= n; i++)
        {
            scanf("%d", &c);
            sum1 += c;
            Tu::addedge(s, i, c);
        }
        int t = Tu::t = n + m + 1;
        for (int i = 1; i <= m; i++)
        {
            scanf("%d", &c);
            sum2 += c;
            Tu::addedge(i + n, t, c);
        }
        for (int i = n; i >= 1; i--)
            for (int j = m; j >= 1; j--)          //因为BuildAnswer()遍历边的时候是按照先加入后遍历的
                Tu::addedge(i, j + n, 1); //所以为了满足字典序，我们就从后往前加边
        Tu::dinic();
        int maxflow = Tu::maxflow;
        if (sum1 != sum2 || maxflow != sum1)
        {
            puts("Impossible\n");
            continue;
        }
        Tu::BuildAnswer();
        putchar('\n');
    }
}