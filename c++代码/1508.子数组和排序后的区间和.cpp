#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int rangeSum(vector<int> &nums, int n, int left, int right)
    {
        vector<int> sum_vec(nums);
        for (long long i = 0; i < n; i++)
        {
            long long tmp_sum = nums[i];
            for (long long j = i + 1; j < n; j++)
            {
                tmp_sum += (nums[j] % 1000000007);
                tmp_sum %= 1000000007;
                sum_vec.push_back(tmp_sum);
            }
        }
        sort(sum_vec.begin(), sum_vec.end());
        long long ans = 0;
        for (int i = left; i <= right; i++)
        {
            printf("%d\t", sum_vec[i - 1]);
            ans += sum_vec[i - 1] % 1000000007;
            ans %= 1000000007;
        }
        return ans;
    }
};