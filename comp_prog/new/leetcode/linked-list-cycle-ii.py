# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if not flag and slow == fast:
                slow = head 
                flag = True
                break
        
        while flag:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
             
        return None
        