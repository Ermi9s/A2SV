# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next and n > 0:
            return None

        r = head
        for _ in range(n):
            r = r.next
       
        l = head

        if not r:
            head = head.next
            return head

        while r:
            l = l.next
            r = r.next

        ref = head

        while ref.next != l:
            ref = ref.next
        
        ref.next = ref.next.next
        


        return head

        