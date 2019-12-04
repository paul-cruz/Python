from Node import Node

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def empty(self):
        return self.first == None

    def add(self, value):
        if self.empty():
            self.first = self.last = Node(value)
        else:
            aux = self.last
            self.last  = aux.next = Node(value)
            self.last.before = aux
        self.size += 1
    
    def insert(self,value):
        if self.empty():
            self.first = self.last = Node(value)
        else:
            aux = Node(value)
            aux.next = self.first
            self.first.before = aux
            self.first = aux
        self.size += 1

    def print(self):
        aux = self.first
        while aux != None:
            print(aux.value)
            aux = aux.next

    def rprint(self):
        aux = self.last
        while aux != None:
            print(aux.value)
            aux = aux.before

    def get_size(self):
        return self.size

    def remove(self):
        if self.empty():
            print('Empty List')
            return
        elif self.first.next == None:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.before = None
        self.size -= 1

    def pop(self):
        if self.empty():
            print('Empty List')
            return
        elif self.first.next == None:
            self.first = self.last = None
        else:
            self.last = self.last.before
            self.last.next = None
        self.size -= 1
