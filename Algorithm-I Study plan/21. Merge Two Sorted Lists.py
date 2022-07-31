# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        itr1 = list1
        itr2 = list2
        itr3 = itr = ListNode()
        while itr1 and itr2:
            if itr1.val >= itr2.val:
                itr3.next = itr2
                itr2 = itr2.next
                itr3 = itr3.next
            elif itr1.val < itr2.val:
                itr3.next = itr1
                itr1 = itr1.next
                itr3 = itr3.next
        if itr1 or itr2:
            itr3.next = itr1 if itr1 else itr2
        return itr.next
