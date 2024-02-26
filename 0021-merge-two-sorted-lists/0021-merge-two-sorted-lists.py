# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        
        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next
           
        current = head
        while list1 and list2:
            print(current.val)
            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next
                
        if not list2:
            current.next = list1
        else:
            current.next = list2
            
        return head
            
            
            
        