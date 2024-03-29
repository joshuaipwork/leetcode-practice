# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (root2 and not root1):
            return False
        if root1.val != root2.val:
            return False

        left_same = self.isSameTree(root1.left, root2.left)
        if not left_same:
            return False
        right_same = self.isSameTree(root1.right, root2.right)
        return right_same
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()
            if self.isSameTree(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return False
    