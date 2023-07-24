# lesson: the diameter of a tree is the length of the longest path from one leaf node to another.
# the path may or may not go through the root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diam_helper(root)[1]

    def diam_helper(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if not root:
            return 0, 0
        
        # recursive step
        depth_l, diam_l = self.diam_helper(root.left)
        depth_r, diam_r = self.diam_helper(root.right)

        # return results for this subtree
        depth = max(depth_l, depth_r) + 1
        diam = max(depth_l + depth_r, max(diam_l, diam_r))

        return depth, diam
        