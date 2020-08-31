#include <iostream>
#include <string>
#include <map>
using namespace std;

class Solution
{
public:
    string intToRoman(int num)
    {
        map<int, string, greater<int> > roman_map;
        string ans_str = "";
        roman_map[1000] = "M";
        roman_map[900] = "CM";
        roman_map[500] = "D";
        roman_map[400] = "CD";
        roman_map[100] = "C";
        roman_map[90] = "XC";
        roman_map[50] = "L";
        roman_map[40] = "XL";
        roman_map[10] = "X";
        roman_map[9] = "IX";
        roman_map[5] = "V";
        roman_map[4] = "IV";
        roman_map[1] = "I";
        for (auto iter = roman_map.begin(); iter != roman_map.end(); ++iter)
        {
            while (num >= iter->first)
            {
                num -= iter->first;
                ans_str += iter->second;
            }
        }
        return ans_str;
    }
};

int main()
{
    Solution s;
    cout << s.intToRoman(1);
    return 0;
}