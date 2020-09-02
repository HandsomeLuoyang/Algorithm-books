# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left_node = right_node = head
        for i in range(n-1):
            right_node = right_node.next
        if not right_node.next:
            return left_node.next
        
        tmp_node = None
        while right_node.next:
            tmp_node = left_node
            left_node = left_node.next
            right_node = right_node.next
        tmp_node.next = left_node.next
        return head