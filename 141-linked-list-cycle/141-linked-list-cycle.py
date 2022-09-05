# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #traverse over the linkedlist then store in hashset
        #if the item to be stored already exists -> true
        
        exist = set()
        current = head
        while current:
            if current in exist:
                return True
            exist.add(current)
            current = current.next
        return False
            
        