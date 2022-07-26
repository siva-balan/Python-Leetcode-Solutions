# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current  = head
        count = 0
        
        while current:
            count +=1
            current = current.next
        current  = head    
        x =0
        while current.next and x < (count//2):
            x +=1
            current = current.next
            
        return current
