# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def delete(ptr):
            ptr.next = ptr.next.next
        
        temp = head

        while temp and temp.next:
            if temp.val == temp.next.val:
                delete(temp)
            else:
                temp = temp.next
        
        return head