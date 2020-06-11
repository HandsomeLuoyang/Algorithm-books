# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 染色标记法
        # cur_node = head
        # while cur_node:
        #     if cur_node.val != float('inf'):
        #         cur_node.val = float('inf')
        #         cur_node = cur_node.next
        #     else:
        #         return cur_node
        # 快慢指针（情人相遇）法
        # 龟兔在同一起点
        p_slow, p_fast = head, head
        while p_fast and p_fast.next:
            # 兔子每次跑两步，乌龟每次爬一步
            p_slow, p_fast = p_slow.next, p_fast.next.next
            # 如果兔子追上了乌龟，说明有环
            if p_slow is p_fast:
                # 在起点处重新开启一个指针
                start = head
                # 两个指针相遇的地方一定就是环的起点
                # 别问，问就是数学算出来的，自己去算
                while not start is p_slow:
                    start, p_slow = start.next, p_slow.next
                return start