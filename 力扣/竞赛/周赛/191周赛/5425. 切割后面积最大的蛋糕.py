class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list, verticalCuts: list) -> int:
        horizontalCuts.sort()
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)

        verticalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)

        max_h = 0
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i-1])
        
        max_w = 0 - max_h
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i-1])
        
        return (max_h * max_w) % (10**9 + 7)

sol = Solution()
print(sol.maxArea(5, 4, [3], [3]))