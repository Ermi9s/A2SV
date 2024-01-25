# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        if not head:
            return None
        if not head.next:
            return head
        if head.next.next:
            head.next

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next:
            slow = slow.next
        
        return slow