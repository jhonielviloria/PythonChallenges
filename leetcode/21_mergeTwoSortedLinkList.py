"""Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = start = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        merged.next = l1 or l2
        return start.next
