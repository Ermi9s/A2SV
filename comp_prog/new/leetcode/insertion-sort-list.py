# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        bound = dummy.next

        while bound.next:
            bound = bound.next

       
        while bound != head:
            prev = dummy
            curr = dummy.next
            maxi = bound

            while curr != bound:
                if curr.val > maxi.val:
                    maxi = curr

                curr = curr.next
                prev = prev.next
        
            temp = maxi.val
            maxi.val = bound.val
            bound.val = temp
            bound = prev
            
        return dummy.next
                
    



            
        

        