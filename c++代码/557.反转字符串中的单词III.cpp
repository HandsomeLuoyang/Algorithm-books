#include <iostream>
#include <string>
using namespace std;

class Solution
{
public:
    string reverseWords(string s)
    {
        int length = s.length();
        int i = 0, start;
        while (i < length)
        {
            while (i < length && s[i] == ' ')
            {
                i++;
            }
            start = i;
            while (i < length && s[i] != ' ')
            {
                i++;
            }
            int left = start, right = i - 1;
            while (left < right)
            {
                swap(s[left], s[right]);
                left++;
                right--;
            }
        }
        return s;
    }
};

int main()
{
    Solution s;
    cout << s.reverseWords("   Let's go");
    return 0;
}