# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        itr = head
        itr1 = head
        
        while itr1 and itr1.next:
            itr = itr.next
            itr1 = itr1.next.next
            if itr == itr1:
                return True
        return False
