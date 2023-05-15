# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        root = head

        count = []

        while root:
            count.append(root.val)
            root = root.next
        
        count[k-1],count[len(count)-k] = count[len(count)-k],count[k-1]

        final = node = ListNode(count[0])

        for ele in range(1,len(count)):
            node.next = ListNode(count[ele])
            node = node.next
        
        return final
        
