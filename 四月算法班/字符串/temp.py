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

class Sunday(object):
    def __init__(self, pattern:str):
        # 模式串和其长度
        self.pattern, self.length = pattern, len(pattern)
        # 根据模式串构建的偏移字典
        self.shift_dict = {}

        # 构建字典
        for index, value in enumerate(pattern):
            self.shift_dict[value] = self.length - index

    def match(self, text:str):
        i = 0 
        text_length = len(text)
        text += '\0'
        while i <= text_length - self.length:
            j = 0
            while self.pattern[j] == text[i + j]:
                j += 1
                if j >= self.length:
                    return i
            offset = self.shift_dict[text[i+self.length]] if text[i+self.length] in self.shift_dict else self.length + 1
            i += offset
        return -1


import random
import time
sunday = Sunday('helloworld')
kmp = KMP('helloworld')
kmp_average_time = 0
sunday_average_time = 0
for i in range(100):
    ss = ''.join([chr(random.randint(97, 122)) for _ in range(1000000)])

    st = time.process_time()
    sunday.match(ss)
    ed = time.process_time()
    sunday_average_time += ed - st

    st = time.process_time()
    kmp.match(ss)
    ed = time.process_time()
    kmp_average_time += ed - st

print('kmp平均时间: {}'.format(kmp_average_time / 100))
print('sunday平均时间: {}'.format(sunday_average_time / 100))

