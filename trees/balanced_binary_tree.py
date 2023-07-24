# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._isBalancedHelper(root)[0]

    def _isBalancedHelper(self, root: TreeNode) -> tuple[bool, int]:
        """
        A helper function for determining if a binary tree is balanced.

        Parameters:
            root: the root of the subtree to be checked
        Returns:
            tuple of (bool, int): The first element is whether or not this subtree is balanced
                The second element is the depth of this subtree
        """
        # base case
        if not root:
            return True, 0

        # recursive case
        balanced_l, depth_l = self._isBalancedHelper(root.left)
        balanced_r, depth_r = self._isBalancedHelper(root.right)

        # compute for this subtree
        balanced: bool = balanced_l and balanced_r and abs(depth_l - depth_r) < 2
        depth: int = max(depth_l, depth_r) + 1
        
        return balanced, depth