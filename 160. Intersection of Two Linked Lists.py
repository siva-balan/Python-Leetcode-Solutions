class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        r1,r2 = headA,headB
        a,b =0,0
        
        if headA is None or headB is None:
            return
        while r1:
            a +=1
            r1 = r1.next
        while r2:
            b +=1
            r2 = r2.next
        
        x = abs(a-b)
        r1,r2 = headA,headB
        
        if a > b:
            while x > 0:
                r1 = r1.next
                x -=1
        else:
            while x>0:
                r2 = r2.next
                x-=1
        while r1 or r2:
            if r1 == r2:
                return r1
            r1 =r1.next
            r2 = r2.next
        return
