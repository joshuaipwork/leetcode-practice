# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Takeaways:
# order level traversal is useful for finding nodes to the left or right of the tree
# consider edge cases carefully.

# This is an O(n) runtime, since we traverse every node
# This is O(n) memory


import collections
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # def data structures
        queue: collections.deque = collections.deque()
        if root:
            queue.append(root)
        result = []

        # level-order traversal
        # BFS
        while queue:
            node = None

            # traverse the level
            for i in range(len(queue)):
                node = queue.popleft()

                # at each node, add its children to the next level to be traversed
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # the last node in the level gets added to the list
            result.append(node.val)

        # return the list
        return result
