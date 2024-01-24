# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        fir = None
        sec = head
        thr = head.next

        while thr:
            sec.next = fir
            fir = sec
            sec = thr
            thr = thr.next
        sec.next = fir
        return sec


        