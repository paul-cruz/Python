class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def pop(self):
        if not self.empty():
            new_last = self.first
            if new_last.next != None:
                while new_last.next != self.last:
                    new_last = new_last.next
                del new_last.next
                new_last.next = None
                self.last = new_last
            else:
                del self.first
                self.first = None
                self.last = None

    def clear_out(self):
        if not self.empty():
            aux = self.first
            while aux.next != None:
                self.first = aux.next
                del aux
                aux = self.first
            del self.first
            self.first = self.last = None

    def to_list(self):
        l = []
        aux = self.first
        while aux != None:
            l.append(aux.data)
            aux = aux.next
        return l


def change_directory(cwd, cd):
    path = LinkedList()
    for i in cwd.split('/'):
        if i != '':
            path.add(i)

    if cd[0] == '/':
        path.clear_out()
        
    for i in cd.split('/'):
        if i == '..':
            path.pop()
        elif i == '.':
            continue
        else:
            path.add(i)

    if path.empty():
        return '/'

    final_path = '/'.join(path.to_list())
    if final_path[0] != '/':
        final_path = '/' + final_path

    return final_path


if __name__ == "__main__":
    cwd = input()
    cd = input()

    print(change_directory(cwd, cd))
