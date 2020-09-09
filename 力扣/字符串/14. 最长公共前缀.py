class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        pre_lst = []
        index = 0
        try:
            while True:
                s = strs[0][index]
                for ss in strs:
                    if ss[index] != s:
                        return ''.join(pre_lst) if pre_lst else ''
                pre_lst.append(s)
                index += 1
        except Exception as ret:
            return ''.join(pre_lst) if pre_lst else ''

s =Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))