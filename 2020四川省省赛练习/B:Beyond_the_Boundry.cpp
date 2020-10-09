#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void is_zixulie(string ss, vector<string> all_name)
{
    vector<int> tmp;
    for (int t = 0; t < all_name.size(); t++)
    {
        int i = 0, j = 0;
        string tmp_s = all_name[t];
        while (i < tmp_s.size() && j < ss.size())
        {
            if (tmp_s[i] == ss[j])
                j++;
            i++;
        }
        if (j == ss.size()) tmp.push_back(t);
    }
    printf("%d\n", tmp.size());
    for (int i = 0; i < tmp.size(); i++)
    {
        printf("%s\n", all_name[tmp[i]].c_str());
    }
    

}

int main()
{
    vector<string> name_lst;
    name_lst.push_back("Kanbara Akihito");
    name_lst.push_back("Kuriyama Mirai");
    name_lst.push_back("Nase Hiroomi");
    name_lst.push_back("Nase Mitsuki");

    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        string ss;
        cin >> ss;
        is_zixulie(ss, name_lst);
    }

    return 0;
}