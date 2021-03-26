class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DLList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def empty(self):
        return self.length == 0

    def push(self, node):
        if self.empty():
            self.first = self.last = node
        else:
            self.first.prev = node
            node.next = self.first
            self.first = node
        self.length += 1

    def pop(self):
        node = self.last
        key = node.key
        self.last = node.prev
        self.last.next = None
        del node
        self.length -= 1
        return key

    def delete(self, node):
        prev = node.prev
        next = node.next
        node.prev = node.next = None
        if prev:
            prev.next = next
            if next:
                next.prev = prev
            else:
                self.last = prev
        else:
            if next:
                next.prev = None
                self.first = next
            else:
                self.first = self.last = None
        self.length -= 1

    def move_to_front(self, node):
        self.delete(node)
        self.push(node)
    
    def print(self):
        l_aux= []
        aux = self.first
        while aux != None:
            l_aux.append(aux.key)
            aux = aux.next
        print(l_aux)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = DLList()
        self.map = {}

    def get(self, key: int):
        requested_node = self.map.get(key)
        if requested_node:
            self.cache.move_to_front(requested_node)
            #self.cache.print()
            return requested_node.value
        return None

    def put(self, key: int, value: int):
        existing_node = self.map.get(key)
        if existing_node == None:
            new_node = Node(key, value)
            self.cache.push(new_node)
            self.map[key] = new_node
            if self.cache.length > self.capacity:
                self.map.pop(self.cache.pop())
        else:
            existing_node.value = value
            self.cache.move_to_front(existing_node)
        #self.cache.print()

if __name__ == "__main__":
    cache =  LRUCache(2)

    """
    cache.put(1, 1)
    cache.put(2, 2)
    print("GET---", cache.get(1)) #returns 1
    cache.put(3, 3) #evicts key 2
    print("GET---", cache.get(2)) #returns - 1 (not found)
    cache.put(4, 4) #evicts key 1
    print("GET---", cache.get(1)) #returns - 1 (not found)
    print("GET---", cache.get(3)) #returns 3
    print("GET---", cache.get(4)) #returns 4"""

    print("GET---",cache.get(2))
    cache.put(2,6)
    print("GET---",cache.get(1))
    cache.put(1,5)
    cache.put(1,2)
    print("GET---",cache.get(1))
    print("GET---",cache.get(2))
