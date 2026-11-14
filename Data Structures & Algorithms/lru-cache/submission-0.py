class Node:
    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node: Node): # Insert at the beginning of cache
        prev, next = self.right.prev, self.right # Get the right 2 elements
        prev.next = next.prev = node
        node.next, node.prev = next, prev
    
    def remove(self, node: Node):# Remove from position in linked list
        next, prev = node.next, node.prev
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # remove node
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # Instantiate new node
        self.insert(self.cache[key]) # Add new node to right
        
        if len(self.cache) > self.cap: # Cleanup cache LRUCache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        