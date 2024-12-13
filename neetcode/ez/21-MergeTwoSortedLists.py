# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Problem:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current = head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                # current = current.next
                list1 = list1.next
            else:
                current.next = list2
                # current = current.next
                list2 = list2.next
            current = current.next

        # current.next = list1 if not list2 else list2
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        return head.next