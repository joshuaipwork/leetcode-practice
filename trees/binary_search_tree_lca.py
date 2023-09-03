# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Takeaways:
# A binary search tree has the property that all nodes in the left subtree of any node N
# have a value less than N, and all nodes in the right subtree of N have a value greater than N
# This allows us to do O(log n) insert, remove, and searches. This is just a special subset of
# search where we use this property to check if it's the LCA.


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node
