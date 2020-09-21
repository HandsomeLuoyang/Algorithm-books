class Solution:
    def maxSumRangeQuery(self, nums: list, requests: list) -> int:
        if not requests or not nums:
            return 0
        count_dct = {}
        ans = 0
        for item in requests:
            for i in range(item[0], item[1]+1):
                if i not in count_dct:
                    count_dct[i] = 1
                else:
                    count_dct[i] += 1
        count_dct = sorted(count_dct.items(), key=lambda x:x[1], reverse=True)
        nums.sort(reverse=True)
        for i in range(len(count_dct)):
            ans += count_dct[i][1] * nums[i]
        return ans % (10**9 + 7)

s = Solution()
print(s.maxSumRangeQuery([1,2,3,4,5,10], [[0,2],[1,3],[1,1]]))