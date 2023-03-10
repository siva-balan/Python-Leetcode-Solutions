# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.l = 0
        node = self.head
        while node:
            self.l +=1
            node = node.next
        
    def getRandom(self) -> int:
        node = self.head
        x = random.randint(1,self.l)
        cl = 0
        while node:
            cl +=1
            if x == cl:
                return node.val
            node = node.next


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
