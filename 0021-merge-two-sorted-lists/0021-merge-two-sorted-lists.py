# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1 
        
        curr1 = list1
        curr2 = list2
        
        if curr1.val <= curr2.val:
            result = curr1
            curr1 = curr1.next
        else:
            result = curr2
            curr2 = curr2.next
            
        reshead = result
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                result.next = curr1
                curr1 = curr1.next
            else:
                result.next = curr2
                curr2 = curr2.next
            result = result.next
        
        if not curr1:
            result.next = curr2
        
        if not curr2:
            result.next = curr1
        
        return reshead
                
        