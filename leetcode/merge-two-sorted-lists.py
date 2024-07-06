# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    rslt = ListNode()
    tail = rslt
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            self.tail.next = list2
            return self.rslt.next
        if not list2:
            self.tail.next = list1
            return self.rslt.next
        
        first = list1
        sec = list2

        if first.val >= sec.val:
            list2 = list2.next
            sec.next = None
            self.tail.next = sec

        else:
            list1 = list1.next
            first.next = None
            self.tail.next = first
        
        self.tail = self.tail.next

        return self.mergeTwoLists(list1 , list2)
        

        

        

        


        


        