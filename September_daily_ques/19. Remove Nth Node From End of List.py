# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr = head
        count = 0
        
        while itr:
            count +=1
            itr = itr.next
        if count-n==0:
            head = head.next
        
        itr = head
        x =0
        while itr:
            if x == count -n-1 and itr.next.next != None:
                itr.next = itr.next.next
                break
            if x == count -n-1 and itr.next.next == None:
                itr.next = None
                break
            itr = itr.next
            x +=1
        
        itr = head
        return itr
