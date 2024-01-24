# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2
        
        if not one:
            return two
        if not two:
            return one

        if one.val <= two.val:
            merged = Node(one.val)
            one = one.next
        else:
            merged = Node(two.val)
            two = two.next
        mh = merged
        temp = mh

        while one and two:
            if one.val <= two.val:
                newNode = Node(one.val)
                one = one.next
            else:
                newNode = Node(two.val)
                two = two.next

            temp.next = newNode
            temp = temp.next

        while one:
            newNode = Node(one.val)
            temp.next = newNode
            one = one.next
            temp = temp.next

        while two:
            newNode = Node(two.val)
            temp.next = newNode
            two = two.next
            temp = temp.next
        
        return mh
            



        
        


        