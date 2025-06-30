# Leetcode no 234 : Palindrome Linked List

from typing import Optional

# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        storage = []
        curr = head 
        while curr:
            storage.append(curr.val)
            curr = curr.next
        
        for i in range (len(storage)//2):
            if storage[i] != storage[-(i+1)]:
                return False
        
        return True
    
    
def main():
    # Create a sample linked list: 1 -> 2 -> 2 -> 1
    node4 = ListNode(1)
    node3 = ListNode(2, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    # Create an instance of Solution
    solution = Solution()

    # Call isPalindrome
    result = solution.isPalindrome(node1)

    # Print result
    print("Is palindrome:", result)

main()

            
# List = [1,2,3]
# print(len(List)/2)

# for i in range (len(List)//2):
#     print("yaya")