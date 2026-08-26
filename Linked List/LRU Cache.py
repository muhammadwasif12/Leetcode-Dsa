class Node:
    def __init__(self, key, val):
        # Cache ki key
        self.key = key

        # Cache ki value
        self.val = val

        # Previous node
        self.prev = None

        # Next node
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        # Cache ki maximum capacity
        self.capacity = capacity

        # HashMap:
        # key -> Node
        self.cache = {}

        # Dummy left node
        # Iske baad LRU node hota hai
        self.left = Node(0, 0)

        # Dummy right node
        # Isse pehle MRU node hota hai
        self.right = Node(0, 0)

        # Initially left aur right directly connected
        self.left.next = self.right
        self.right.prev = self.left

    # Node ko list se remove karna
    def remove(self, node):

        # Node ke previous ko save karo
        prev = node.prev

        # Node ke next ko save karo
        nxt = node.next

        # Previous node ko next se connect karo
        prev.next = nxt

        # Next node ko previous se connect karo
        nxt.prev = prev

    # Node ko right/MRU side par add karna
    def insert(self, node):

        # Right ke just pehle node add hoga
        prev = self.right.prev

        # New node ka next = right
        node.next = self.right

        # New node ka previous = old MRU
        node.prev = prev

        # Old MRU ka next = new node
        prev.next = node

        # Right ka previous = new node
        self.right.prev = node

    def get(self, key):

        # Agar key cache mein nahi hai
        if key not in self.cache:
            return -1

        # HashMap se node directly mil jayegi
        node = self.cache[key]

        # Kyunki node use hui hai,
        # ye ab most recently used banegi

        # Pehle current position se remove karo
        self.remove(node)

        # Phir right/MRU side par add karo
        self.insert(node)

        # Node ki value return karo
        return node.val

    def put(self, key, value):

        # Agar key already cache mein hai
        if key in self.cache:

            # Existing node ko remove karo
            self.remove(self.cache[key])

        # New node banao
        node = Node(key, value)

        # HashMap mein store karo
        self.cache[key] = node

        # New node ko MRU side par add karo
        self.insert(node)

        # Agar capacity exceed ho gayi
        if len(self.cache) > self.capacity:

            # Left ke just baad wala node = LRU
            lru = self.left.next

            # LRU ko linked list se remove karo
            self.remove(lru)

            # HashMap se bhi remove karo
            del self.cache[lru.key]
