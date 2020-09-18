#include <iostream>
using namespace std;

void helper(int n)
{
    if (n==0) return ;
    int tmp = n % 10;
    helper(n/10);
    cout<<tmp<<endl;
}

int main()
{
    int n;
    cin>>n;
    helper(n);
    return 0;
}