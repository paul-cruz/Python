from Node import Node

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def empty(self):
        return self.first == None

    def add(self, data):
        if self.empty():
            self.first = self.last = Node(data)
        else:
            self.last.next = self.last = Node(data)

    def insert(self, data):
        if self.empty():
            self.first = self.last = Node(data)
        else:
            aux = self.first
            self.first = Node(data)
            self.first.next = aux

    def pop(self):
        aux = self.first
        while aux.next != self.last:
            aux = aux.next
        del aux.next
        aux.next = None
        self.last = aux

    def remove(self):
        aux = self.first
        self.first = self.first.next
        del aux
    
    def print_list(self):
        aux = self.first
        while aux != None:
            print(aux.data)
            aux = aux.next

    def search(self, data):
        aux = self.first
        while aux.next != None:
            if aux.data == data:
                return True
            aux = aux.next
        return aux.data == data

    def locate(self, data):
        pos, aux = 0, self.first
        while aux.next != None:
            if aux.data == data:
                return pos
            aux = aux.next
            pos+=1
        return -1
        
    def clear_out(self):
        aux = self.first
        while aux.next != None:
            self.first = aux.next
            del aux
            aux = self.first
        del self.first
        self.first = self.last = None