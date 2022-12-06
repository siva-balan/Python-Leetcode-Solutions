class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        n = 0
        x = head
        while x:
            n +=1
            x = x.next
