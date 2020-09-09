# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left_node = right_node = head
        for i in range(n):
            right_node = right_node.next
        if not right_node.next:
            return left_node.next
        while right_node.next:
            left_node = left_node.next
            right_node = right_node.next
