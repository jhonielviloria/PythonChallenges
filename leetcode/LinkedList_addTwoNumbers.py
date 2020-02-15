# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def setNext(self, n):
        self.next = n


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        while True:
            num1 = str(l1.val) + num1
            if l1.next == None: break
            l1 = l1.next

        while True:
            num2 = str(l2.val) + num2
            if l2.next == None: break
            l2 = l2.next

        sum = str(int(num1) + int(num2))
        prev = None
        for i in range(len(sum)):
            curr = ListNode(sum[i])
            curr.next = prev
            prev = curr
        return curr
