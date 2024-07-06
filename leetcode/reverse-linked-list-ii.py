# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left -= 1
        right -= 1

        if not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        def reverse(h):
            prv = None
            curr = h
            
            while curr:
                nxt = curr.next
                curr.next = prv
                prv = curr
                curr = nxt
                
            return prv
      
        l = head
        r = head
        for _ in range(left):
            prev = prev.next
            l = l.next
        for _  in range(right):
            r = r.next
        
        hold = r.next
        r.next = None
     
        reved = reverse(l)

        prev.next = reved
        
        while prev.next:
            prev = prev.next
        
        prev.next = hold

        return dummy.next


            
            
        

        

        