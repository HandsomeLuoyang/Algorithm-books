from collections import Counter

class Solution:
    def topKFrequent(self, nums: list, k: int):
        return [x[0] for x in Counter(nums).most_common()[:k]]

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))