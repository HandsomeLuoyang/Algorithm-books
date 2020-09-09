from collections import Counter


class Solution:
    def numTriplets(self, nums1:list, nums2:list) -> int:
        nums1_pf = Counter(map(lambda x: x**2, nums1))
        nums2_pf = Counter(map(lambda x: x**2, nums2))
        nums1.sort()
        nums2.sort()

        ans = 0

        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                if nums2[i] * nums2[j] in nums1_pf:
                    ans += nums1_pf[nums2[i] * nums2[j]]
                if nums2[i] * nums2[j] > max(nums1_pf):
                    break
        
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                if nums1[i] * nums1[j] in nums2_pf:
                    ans += nums2_pf[nums1[i] * nums1[j]]
                if nums1[i] * nums1[j] > max(nums2_pf):
                    break
        
        return ans

s = Solution()
print(s.numTriplets([7,7,8,3], [1,2,9,7]))