class Solution:
    def sumOddLengthSubarrays(self, arr: list) -> int:
        ans = 0
        length = 1
        while length <= len(arr):
            for i in range(len(arr)):
                if i + length > len(arr):
                    break
                ans += sum(arr[i:i+length])
            length += 2
        
        return ans

s = Solution()
print(s.sumOddLengthSubarrays([1,4,2,5,3]))