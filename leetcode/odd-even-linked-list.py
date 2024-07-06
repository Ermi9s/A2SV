# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        mark = ListNode("#")
        def throw(ptr , tail):
            temp = ptr.next
            ptr.next = ptr.next.next
            temp.next = None
            tail.next = temp
            
        
        tail = head

        while tail.next:
            tail = tail.next

        tail.next = mark
        tail = tail.next

        toggle = True

        ptr = head

        while ptr.next.val != "#":
            throw(ptr,tail) 
            if ptr.next.val == "#":
                break
            ptr = ptr.next
            tail = tail.next
        
        ptr.next = ptr.next.next

        return head

        

        