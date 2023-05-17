# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        output = 0

        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)

        for i in range(0,n//2):
            if arr[i] + arr[n-1-i] > output:
                output = arr[i] + arr[n-1-i]
        
        return output
