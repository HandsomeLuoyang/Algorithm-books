class Solution:
    def intToRoman(self, num: int) -> str:
        #时间复杂度O(1),空间复杂度为O(1)
        d = {1000:'M',900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        result = ''
        for i in d:
            while num >= i:
                num -= i
                result += d[i]
        return result
