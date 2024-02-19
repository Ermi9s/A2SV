# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        def remove(prv , cur):
            prv.next = cur.next
            cur.next = None
            return cur

        
        dummy = ListNode()
        dummy.next = head 

        temp = head

        while temp.next:
            temp = temp.next
        
        tail = temp
        mark = ListNode('#')
        tail.next = mark
        tail = tail.next

        prev = dummy
    
        while prev.next.val != '#':
            removed = False
            curr = prev.next
            if curr.val >= x:
                node = remove(prev , curr)
                tail.next = node
                tail = tail.next
                removed = True
            
            if not removed: 
                prev = prev.next
        
        remove(prev , prev.next)

        return dummy.next

