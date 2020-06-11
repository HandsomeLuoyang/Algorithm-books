class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) <= 1:
            return 0
        # 维护一个最小值
        min_ = prices[0]
        # 维护利润最大值
        max_pro = 0
        
        for i in range(1, len(prices)):
            max_pro = max(max_pro, prices[i] - min_)
            min_ = min(min_, prices[i])
        return max_pro