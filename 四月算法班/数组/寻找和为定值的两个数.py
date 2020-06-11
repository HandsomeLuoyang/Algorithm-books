# 输入一个数组和一个数字target，在数组中寻找和为target的两个数。

def sum_target(nums:list, target:int):
    val_dict = {}
    for i in range(len(nums)):
        if (target - nums[i]) in val_dict:
            return val_dict[target-nums[i]], i
        else:
            val_dict[nums[i]] = i
    return -1, -1

print(sum_target([1,3,4,7,5,8], 12))