#include <iostream>
#include <time.h>
using namespace std;

void baoli(int n)
{
    // �����������
    unsigned long long sum_ = 0;
    for (int i = 1; i <= n; i++)
    {
        int tmp_num = 1;
        for (int j = 1; j <= i; j++)
        {
            tmp_num *= j;
        }
        sum_ += tmp_num;
        sum_ %= 1000000007;
    }
    printf("������: %lld\n", sum_);
}

void youhua(int n)
{
    // �Ż���ķ������
    unsigned long long sum_ = 0;
    int tmp_mul = 1;
    for (int i = 1; i <= n; i++)
    {
        tmp_mul *= i;
        sum_ += tmp_mul;
        sum_ %= 1000000007;
    }
    printf("�Ż���ķ���: %lld\n", sum_);
}

int main()
{
    int num;
    clock_t start, finish;
    scanf("%d", &num);
    start = clock();
    baoli(num);
    finish = clock();
    double duration = (double)(finish - start) / CLOCKS_PER_SEC;
    printf("%f seconds\n", duration);

    start = clock();
    youhua(num);
    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    printf("%f seconds\n", duration); 
    return 0;
}