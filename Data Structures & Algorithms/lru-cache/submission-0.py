class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key maps to a node

        #left is LRU, right is MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev

    # insert at rightmost pos
    def  insert(self, node):
        curr = self.right.prev
        curr.next = self.right.prev = node
        node.prev, node.next = curr, self.right


    def get(self, key: int) -> int:
        if key in self.cache:
            #update to MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

