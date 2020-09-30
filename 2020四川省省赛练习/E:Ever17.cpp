#include <iostream>
#include <string>
#include <cstdio>
#include <math.h>
using namespace std;

const int month_days[13] = {-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const string month_english[13] = {"-1", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

int isLeapYear(int year)
{
    return ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);
}

void dataHandle(int a, int b, int c)
{
    int year1 = -1;
    int year2 = -1;
    int month1 = -1;
    int month2 = -1;
    int day1 = -1;
    int day2 = -1;
    // 假设是MM/DD/YY
    if (a <= 12 && b <= (a == 2 ? month_days[a] + isLeapYear(2000 + c) : month_days[a]))
    {
        year1 = 2000 + c;
        month1 = a;
        day1 = b;
    }
    // 假设是YY/MM/DD
    if (b <= 12 && c <= (b == 2 ? month_days[b] + isLeapYear(2000 + a) : month_days[b]))
    {
        year2 = 2000 + a;
        month2 = b;
        day2 = c;
    }
    if (year1 != -1 && year2 != -1)
    {
        // 判断两个日期是否相等
        if (year1 == year2 && month1 == month2 && day1 == day2)
            printf("%s %d, %d\n", month_english[month1].c_str(), day1, year1);
            return ;
        // 判断两个日期谁大, 1默认代表日期1大
        int flag = 1;
        // 两者之间间隔天数
        int interval = 0;
        if (year1 < year2 || (year1 <= year2 && month1 < month2) || (year1 <= year2 && month1 <= month2 && day1 < day2))
            flag = 0;
        
        if (flag == 1)
        {
            while (year1 != year2 && month1 != month2 && day1 != day2)
            {

            }
        }
    }

    if (year2 == -1)
    {
        printf("%s %d, %d\n", month_english[month1].c_str(), day1, year1);
        return;
    }
    if (year1 == -1)
    {

        printf("%s %d, %d\n", month_english[month2].c_str(), day2, year2);
        return;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int a, b, c;
        scanf("%d/%d/%d", &a, &b, &c);
        printf("%d, %d, %d\n", a, b, c);
        dataHandle(a, b, c);
    }

    return 0;
}