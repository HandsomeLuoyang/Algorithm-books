class KMP():
    def __init__(self, ss: str) -> list:
        self.length = len(ss)
        self.next_lst = [0 for _ in range(self.length)]
        self.next_lst[0] = -1
        i = 0
        j = -1
        while i < self.length - 1:
            if j == -1 or ss[i] == ss[j]:
                i += 1
                j += 1
                if ss[i] == ss[j]:
                    self.next_lst[i] = self.next_lst[j]
                else:
                    self.next_lst[i] = j
            else:
                j = self.next_lst[j]
        self.pattern = ss
    
    def match(self, ss:str):
        ans_lst = []
        j = 0
        for i in range(len(ss)):
            if ss[i] != self.pattern[j]:
                j = self.next_lst[j] if self.next_lst[j] != -1 else 0
            if ss[i] == self.pattern[j]:
                j += 1
            if j == self.length:
                return i + 1 - self.length
        return -1


s = KMP('nihao')

import time
from 字符串匹配串 import ss

st = time.process_time()
print('匹配位置：', s.match(ss))
ed = time.process_time()
print('Used time: {}'.format(ed - st))