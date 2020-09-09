class Solution:
    def modifyString(self, s: str) -> str:
        ss = list(s)
        char_26 = [chr(x) for x in range(97, 123)]
        # 特判
        if ss[0] == '?':
            if len(ss) == 1:
                return 'a'
            else:
                if ss[1] != 'a':
                    ss[0] = 'a'
                else:
                    ss[0] = 'b'
        
        if ss[-1] == '?':
            if ss[-2] != 'a':
                ss[-1] = 'a'
            else:
                ss[-1] = 'b'

        
        for i in range(1, len(ss)):
            if ss[i] == '?':
                for j in char_26:
                    if i + 1 < len(ss) and j != ss[i-1] and j != ss[i+1]:
                        ss[i] = j
                        break
                    elif i + 1 >= len(ss) and j != ss[i-1]:
                        ss[i] = j
                        break
        
        return ''.join(ss)



s = Solution()
print(s.modifyString('h?a?aaaa??????'))
