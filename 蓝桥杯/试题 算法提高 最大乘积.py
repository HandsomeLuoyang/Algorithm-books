def fun(m,nums):
    nums.sort()  # 从小到大排序 有负数的话，负数在左边
    # 在m=1的情况下，直接返回最大值即可
    if m == 1:
        return nums[-1]
    s = 1
    start = 0 
    end = len(nums) - 1  
    while start < len(nums)-2 and end > 0 and m > 0:
        # 两个负数的乘积大于等于两个正数的乘积
        if nums[start] * nums[start+1] >= nums[end] * nums[end-1] and m >= 2:
            s *= nums[start] * nums[start+1]
            start += 2
            m -= 2
        # 否则取数值最大的数
        else:
            s *= nums[end]
            end -= 1
            m -= 1
    return s

if __name__ == "__main__":
    n = int(input()) # 数组的个数
    total = []
    while n > 0:
        a = li6t(map(int,input().split()))
        b = list(map(int,input().split()))
        total.append(fun(a[1],b))
        n -= 1
    for i in total:
        print(i)
