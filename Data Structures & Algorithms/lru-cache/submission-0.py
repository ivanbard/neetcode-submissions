class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}

        # dummys 
        self.left = Node(0, 0) #least recently used
        self.right = Node(0, 0) #most recently used

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        # insert right before most recently used
        previous_mru = self.right.prev

        previous_mru.next = node
        node.prev = previous_mru

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1

        node = self.table[key]

        # since accessed, its now the most recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            old_node = self.table[key]
            self.remove(old_node)

        node = Node(key, value)

        self.table[key] = node
        self.insert(node)

        #too many items, remove least recently used
        if len(self.table) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.table[lru.key]