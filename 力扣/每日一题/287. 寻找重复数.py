class Solution:
    def findDuplicate(self, nums: list) -> int:
        """
        同链表里的142.环形链表：
        快慢指针（情人相遇）法
        """
        p_slow, p_fast = 0, 0
        while True:
            p_slow = nums[p_slow]
            p_fast = nums[nums[p_fast]]

            if nums[p_slow] == nums[p_fast]:
                start = 0
                while nums[start] != nums[p_slow]:
                    start = nums[start]
                    p_slow = nums[p_slow]
                return nums[start]