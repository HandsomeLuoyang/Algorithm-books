class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for ss in s:
            if ss == 'A':
                x = 2 * x + y
            elif ss == 'B':
                y = 2 * y + x
        return x + y