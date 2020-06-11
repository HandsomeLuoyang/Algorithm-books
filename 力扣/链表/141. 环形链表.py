# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p_slow, p_fast = head, head
        while p_fast and p_fast.next:
            p_slow, p_fast = p_slow.next, p_fast.next.next
            if p_slow is p_fast:
                return True
        return False