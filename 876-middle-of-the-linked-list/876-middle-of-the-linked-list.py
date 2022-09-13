# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        node = head
        length = 0
        while current:
            length += 1
            current = current.next
        mid = length // 2
        counter = 0
        while node:
            if counter == mid:
                return node
            else:
                counter+=1
                node = node.next
        return None
                
        