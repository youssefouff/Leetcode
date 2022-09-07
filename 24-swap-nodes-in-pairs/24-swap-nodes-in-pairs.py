# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        create dummy node with dummy pointer, then check we have pairs(even length)
        
        """
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr and curr.next:
            #assign pointers
            nextPair = curr.next.next
            second = curr.next
            #reverse pointers
            second.next = curr
            curr.next = nextPair
            prev.next = second
            #update pointers
            prev = curr
            curr = nextPair
        return dummy.next
            
            
        