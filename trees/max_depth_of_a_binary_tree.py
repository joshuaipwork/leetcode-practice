# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthRecursive(self, root: Optional[TreeNode]) -> int:
        """
        Memory: O(n)
        Runtime: O(n)

        Recursive Solution
        """
        if root is None:
            return 0
        return max(self.maxDepthRecursive(root.left), self.maxDepthRecursive(root.right)) + 1
    def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
        """
        Memory: O(n)
        Runtime: O(n)
        Iterative DFS
        """
        stack: list[TreeNode] = []
        stack.append((root, 1))
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth
    def maxDepthIterativeBFS(self, root: Optional[TreeNode]) -> int:
        """
        Memory: O(n)
        Runtime: O(n)
        Iterative BFS
        """
        queue: list[TreeNode] = []
        queue.append((root, 1))
        max_depth = 0

        while queue:
            node, depth = queue.pop(0)
            
            if node:
                max_depth = max(max_depth, depth)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return max_depth        