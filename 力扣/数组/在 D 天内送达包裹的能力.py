class Solution:
    def is_ok(self, weights, current_weight, D):
        current_day = 1
        index_weight = 0
        for i in weights:
            if index_weight + i <= current_weight:
                index_weight += i
            else:
                current_day += 1
                index_weight = i
        if current_day < D:
            return '太大'
        elif current_day > D:
            return '太小'
        else:
            return 'ok'

    def shipWithinDays(self, weights: list, D: int) -> int:
        """采用二分法"""
        lo = max(weights)
        hi = sum(weights)
        ans = -1
        while lo < hi:
            # 如果偏大或者相等，那就继续往小的找,但是相等的时候要记录答案，如果偏小，就往大的找
            mid = (lo + hi) // 2
            s = self.is_ok(weights, mid, D)
            if s == '太大':
                if mid == max(weights):
                    return mid
                if lo == hi-1:
                    return ans
                hi = mid
                continue
            elif s == 'ok':
                if lo == hi-1:
                    return ans
                ans = mid
                hi = mid
                continue
            else:
                if lo == hi-1:
                    return hi
                lo = mid
                continue
        return ans



s = Solution()
print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 1))
