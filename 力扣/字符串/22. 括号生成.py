import time


class Solution:
    def generateParenthesis(self, n: int) -> list:
        if n == 0 or n == 1:
            return ['()' for _ in range(n)]
        # 由于python的字符的不可变性，这里用列表代替字符串
        ss_lst = ['_' for i in range(2*n)]
        self.length = 2*n
        # 答案字符串
        self.ans_lst = []

        # 递归
        ss_lst[0] = '('
        self.digui(1, ss_lst, 1)
        return self.ans_lst
    
    def digui(self, start:int, ss_lst:list, need:int):
        # 递归目的:求出所有符合条件的括号组合
        # 结束条件:start == self.length的时候或者need == self.length-start的时候

        # 这一步是由于python对象中列表的性质决定
        ss_lst = ss_lst[:]
        
        # 如果当前剩余空数与需要的右括号数相等，则直接生成返回
        # 递归函数必然是这样终止，因为生成的最后一个括号必然是)
        if need == self.length - start:
            i= 0
            for i in range(start, self.length):
                ss_lst[i] = ')'
            self.ans_lst.append(''.join(ss_lst))
            return
        
        # 找出函数的等价式
        ss_lst[start] = '('
        self.digui(start+1, ss_lst, need+1)
        # 如果需要匹配右括号，则增加一个右括号的递归
        if need != 0:
            ss_lst[start] = ')'
            self.digui(start+1, ss_lst, need-1)


s = Solution()
st = time.process_time()
print(s.generateParenthesis(14))
ed = time.process_time()
print('运行时间：', ed-st)
