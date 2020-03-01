"""Given a linked list, remove the n-th node from the end of list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_head = start = ListNode(0)
        head_copy = head
        cnt = 1
        while head_copy:
            cnt += 1
            head_copy = head_copy.next

        while head:
            cnt -= 1
            if cnt == n:
                if head.next == None:
                    new_head.next = None
                head = head.next
                continue
            new_head.next = head
            new_head = new_head.next
            head = head.next
        return start.next