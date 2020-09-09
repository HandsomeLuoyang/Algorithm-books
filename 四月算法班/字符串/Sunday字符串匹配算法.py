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

s = Sunday('nihao')

import time
# from 字符串匹配串 import ss
st = time.process_time()
print('匹配位置: ', s.match(ss))
ed = time.process_time()
print('Used time: {}'.format(ed - st))