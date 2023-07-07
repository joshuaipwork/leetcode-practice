class MinStackNode:
    def __init__(self, val, last_node):
        self.val = val
        if last_node:
            self.min_at_push = min(val, last_node.min_at_push)
            self.last_node = last_node
        else:
            self.min_at_push = val
            self.last_node = None

class MinStack:
    def __init__(self):
        self.top_node = None

    def push(self, val: int) -> None:
        new_node = MinStackNode(val, self.top_node)
        self.top_node = new_node

    def pop(self) -> None:
        if self.top_node:
            self.top_node = self.top_node.last_node
        else:
            raise IndexError("No elements in the stack to pop")

    def top(self) -> int:
        if self.top_node:
            return self.top_node.val
        else:
            raise IndexError("No elements in the stack")

    def getMin(self) -> int:
        if self.top_node:
            return self.top_node.min_at_push
        else:
            raise IndexError("No elements in the stack to get min of")
