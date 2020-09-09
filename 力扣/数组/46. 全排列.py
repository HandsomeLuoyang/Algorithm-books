# from itertools import permutations

class Solution:
    def permute(self, nums:list) -> list:
        self.ss_lst = nums
        self.ans_lst = []
        # 库函数解决
        # self.ans_lst = list(permutations(nums, len(nums)))
        # return self.ans_lst
        self.permutation(0, len(nums))
        return self.ans_lst
    def permutation(self, from_:int, to_:int):
        # 如果排到了第四个了，就直接打印输出
        if from_ == to_:
            self.ans_lst.append(self.ss_lst[:])
        for i in range(from_, to_):
            # 当前值和下一个值进行交换
            self.ss_lst[i], self.ss_lst[from_] = self.ss_lst[from_], self.ss_lst[i]
            # 当前值固定，让下一个值和下下个值进行交换，循而复之
            self.permutation(from_+1, to_)
            # print('交换前：', self.ss_lst)
            # 换回来，保证不遗漏
            self.ss_lst[i], self.ss_lst[from_] = self.ss_lst[from_], self.ss_lst[i]
            # print('交换后：', self.ss_lst)

s = Solution()
print(s.permute([1, 2, 3]))