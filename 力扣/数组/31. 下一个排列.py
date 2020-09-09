#!usr/bin/python3
class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从右向左搜寻，记录最大值，如果找到某个值比最大值小，记为x，即可交换，交换的时候从右边找到比
        # x大的最小值，进行交换，交换之后对原x位置的右侧进行排序

        # 特判
        length = len(nums)
        if length <= 1:
            return 
        # 记录值
        cur_max = nums[-1]
        huan_index = -1
        cur_large_min = length - 1
        # 标志信息，是否可换
        flag = False
        # 自右向左寻找可能存在的降序
        for i in range(length-2, -1, -1):
            if nums[i] > cur_max:
                cur_max = nums[i]
                cur_large_min = i
            elif nums[i] < cur_max:
                huan_index = i
                flag = True
                break
        # 代表不可换，即已经是字典序的最大值，直接原地逆序
        if not flag:
            nums.reverse()
            return nums
        
        # 代表可以交换，那就先交换后，对右边再排序
        else:
            for i in range(huan_index+1, length):
                if nums[i] > nums[huan_index] and nums[i] < cur_max:
                    cur_large_min = i
            
            # 交换
            nums[huan_index], nums[cur_large_min] = nums[cur_large_min], nums[huan_index]

            # 对huan_index之后的值使用选择排序
            for i in range(huan_index+1, length):
                index  = i
                min_ = nums[i]
                for j in range(i+1, length):
                    if nums[j] < min_:
                        index = j
                        min_ = nums[j]
                nums[i], nums[index] = nums[index], nums[i]
            return nums




s = Solution()

# 也可以加上循环打印全排列
st_nt = [2, 1, 3, 7, 7, 6]
nt = st_nt[:]
while True:
    print(nt)
    nt = s.nextPermutation(nt)
    if st_nt == nt:
            break
    