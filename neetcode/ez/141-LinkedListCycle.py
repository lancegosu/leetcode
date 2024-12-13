# Link: https://leetcode.com/problems/linked-list-cycle/
# Problem:
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be 
# reached again by continuously following the next pointer. Internally, pos is used to 
# denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        # using a list
        # visited = []
        # current = head
        # while current is not None:
        #     visited.append(current)
        #     if current.next in visited:
        #         return True
        #     current = current.next
        
        # return False

        # using two pointers
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            if slow == fast.next:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False