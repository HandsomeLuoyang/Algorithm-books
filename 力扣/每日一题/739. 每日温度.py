class Solution:
    def dailyTemperatures(self, T: list) -> list:
        if len(T) == 1:
            return [0]
        ans_lst = [0] * len(T)
        # 通过一个有序的栈的入栈出栈来实现
        stack = []
        for i, v in enumerate(T):
            while stack and v > stack[-1][1]:
                ans_lst[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            if not stack or v <= stack[-1][1]:
                stack.append((i, v))
        return ans_lst