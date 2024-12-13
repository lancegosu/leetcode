# Link: https://leetcode.com/problems/reverse-linked-list/
# Problem:
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # current = head  # Start at the head node
        # while current is not None:  # While there are more nodes
        #     # Apply logic here
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node  # Move to the next node
        # return prev

        if head is None or head.next is None:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

# Helper function to convert a list into a linked list
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print the linked list (for testing purposes)
def print_linkedlist(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)
    
# Test the reverseList function
check = Solution()
linked_list_head = list_to_linkedlist([1, 2, 3, 4, 5])
reversed_head = check.reverseList(linked_list_head)
print_linkedlist(reversed_head)  # Should print [5, 4, 3, 2, 1]