class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dummy = ListNode(0, None, None) # head is at self.dummy.next
        self.tail = self.dummy
        self.length = 0

    def add_to_end(self, key: int) -> tuple[int, ListNode]:
        # append node to end storing key
        self.tail.next = ListNode(key, None, self.tail)
        self.tail = self.tail.next
        self.length += 1

        # update head if this is the first node to be added
        if self.length == 1:
            self.dummy.next = self.tail

        # evict if overcapacity
        old_head = None
        if self.length > self.capacity:
            old_head = self.dummy.next
            self.dummy = self.dummy.next
            self.length -= 1
        
        return self.tail, old_head
    def move_to_end(self, node: ListNode):
        if node == self.tail:
            return
        prev = node.prev

        prev.next =  node.next
        if node.next:
            node.next.prev = prev

        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        node.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # 
        self.capacity = capacity
        self.RU_list = LinkedList(self.capacity)
        self.hashmap = {}

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        value, node = self.hashmap[key]
        self.RU_list.move_to_end(node)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key] = (value, self.hashmap[key][1])
            self.RU_list.move_to_end(self.hashmap[key][1])
        else:
            added_node, removed_node = self.RU_list.add_to_end(key)
            if removed_node:
                self.hashmap.pop(removed_node.val)
            self.hashmap[key] = (value, added_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)