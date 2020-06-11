class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans_ss = ''
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                ss = ''
                tmp_s = stack.pop()
                while tmp_s != '[':
                    ss += tmp_s
                    tmp_s = stack.pop()
                int_ss = ''
                int_tmp_ss = stack.pop()
                while int_tmp_ss.isdigit():
                    int_ss += int_tmp_ss
                    if len(stack) > 0 and stack[-1].isdigit():
                        int_tmp_ss = stack.pop()
                    else:
                        break
                int_ss = int(int_ss[::-1])
                ss = int_ss * ss[::-1]
                for t in ss:
                    stack.append(t)
        return ''.join(stack)

sol = Solution()
print(sol.decodeString('100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]\
    100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]\
        100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]] \
            100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]\
    100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]\
        100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]] \
            100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]\
    100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]\
        100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]100[a23[d4[a]5[c]2[d]]4[z]]2[2[x3[n]]b2[a2[c]]]'))