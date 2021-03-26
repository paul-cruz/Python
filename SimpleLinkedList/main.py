class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
    
    def empty(self):
        return self.first == None

    def print(self):
        next_node = self.first
        str_ = ''
        while (next_node):
            str_ += str(next_node.value) + ' '
            next_node = next_node.next
        print(str_)

    def append(self, value):
        new_node = Node(value)

        if self.empty():
            self.first = new_node
        else:
            last = self.first
            while last.next:
                last = last.next
            last.next = new_node

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.first
        self.first = new_node
    
    def reverse(self):
        prev_node = None
        next_node = current_node = self.first
        while next_node:
            current_node = next_node
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
        self.first = current_node
           
if __name__ == "__main__":
    list_ = LinkedList()
    list_.append(1)
    list_.append(2)
    list_.append(3)
    list_.print()
    list_.reverse()
    list_.print()
