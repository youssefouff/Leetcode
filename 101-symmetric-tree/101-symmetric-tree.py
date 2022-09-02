# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    
    def isMirror(self, leftC, rightC):
        if leftC and rightC:
            return leftC.val == rightC.val and self.isMirror(leftC.left,rightC.right) and self.isMirror(leftC.right,rightC.left)
        
        return leftC == rightC
        
            
        