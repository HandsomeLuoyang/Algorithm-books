import math

class Solution:
    def numWays(self, s: str) -> int:
        all_cnt_1 = s.count('1')
        if all_cnt_1 % 3 != 0:
            return 0
        
        if all_cnt_1 == 0:
            return ((len(s) - 1) * (len(s) - 2)) // 2 % (10 ** 9 + 7)
        sep_cnt = all_cnt_1 // 3

        sep_cnt_first_0 = 1
        sep_cnt_second_0 = 1

        cur_1 = 0


        i = 0
        while i < len(s):
            if s[i] == '1':
                cur_1 += 1
                if cur_1 == sep_cnt:
                    i += 1
                    break
            i += 1
        
        while i < len(s):
            if s[i] == '0':
                sep_cnt_first_0 += 1
            else:
                cur_1 = 0
                break
            i += 1
        
        while i < len(s):
            if s[i] == '1':
                cur_1 += 1
                if cur_1 == sep_cnt:
                    i += 1
                    break
            i += 1
        
        while i < len(s):
            if s[i] == '0':
                sep_cnt_second_0 += 1
            else:
                break
            i += 1

        
        return (sep_cnt_first_0 * sep_cnt_second_0) % (10 ** 9 + 7) 


s = Solution()
print(s.numWays('00000000'))