# Leetcode no 206 : Reverse Linked List 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
    
        return prev 
            