import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# takeaways:
# Level order traversal via BFS with two nested loops
# deques are faster for queues than lists
# none checking with root, and on insertion is faster


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # def data structures
        queue = (
            collections.deque()
        )  # deques are doubly linked lists, so O(1) pop from head, O(1) append
        output = []

        if root:
            queue.append(root)

        # BFS traversal
        while queue:
            level_list = []

            # the queue contains all nodes in the level.
            # Put all the nodes in that level them in a list and add to our output
            for i in range(len(queue)):
                node = queue.popleft()
                level_list.append(node.val)

                # when traversing, always put left first onto the queue so
                # left is traversed first
                # When we append, they will be traversed in the next run of the outer loop
                # because range(len(queue)) was only the length of the nodes of the current level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level_list)

        return output

    def levelOrderTuples(self, root: Optional[TreeNode]) -> List[List[int]]:
        # def data structures
        queue = [(root, 0)]
        output = []

        # BFS traversal
        level_list = []
        current_level = 0
        while queue:
            node, node_level = queue.pop(0)

            if node is None:
                continue

            # if the level increases, then we append level list to output, create a new level list
            if node_level > current_level:
                output.append(level_list)
                level_list = []
                current_level = node_level

            # at each node, append to the level list
            level_list.append(node.val)

            # when traversing, always put left first onto the queue so
            # left is traversed first
            # append the level of these nodes.
            queue.append((node.left, current_level + 1))
            queue.append((node.right, current_level + 1))

        # append the level list one last time if it exists
        if level_list:
            output.append(level_list)
        return output
