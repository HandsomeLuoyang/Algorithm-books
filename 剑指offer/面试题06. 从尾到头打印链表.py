# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst.reverse()
        return lst

s = Solution()
head = ListNode(1)
head2 = ListNode(3)
head3 = ListNode(2)
head.next = head2
head2.next = head3

print(s.reversePrint(head))