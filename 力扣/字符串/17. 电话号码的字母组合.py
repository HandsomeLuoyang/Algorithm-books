class Solution:
    def letterCombinations(self, digits: str) -> list:
        self.num_str_lst = {'2':'abc', '3':'def', '4':'ghi',
                       '5':'jkl', '6':'mno','7':'pqrs',
                       '8':'tuv', '9':'wxyz'}
        self.ans_list = []
        self.digui('', digits)
        return self.ans_list

    def digui(self, letter, str_digit):
        # 1.明确函数的作用：明确这个函数，要求一串数字对应的字符的组合
        # 2.寻找递归结束的条件：当下一个字符为空值的时候，直接返回，不递归
        if len(str_digit) == 0:
            return 
        # 3.找出函数的等价关系式（缩小参数范围）：下一个函数等于当前函数处理数字的每一个字符加上
        for lt in self.num_str_lst[str_digit[0]]:
            if len(str_digit) == 1:
                self.ans_list.append(letter+lt)
            self.digui(letter+lt, str_digit[1:])

s = Solution()
s.letterCombinations('23')