class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def tour(node):
    while node != None:
        print(node.data)
        node = node.next

if __name__ == "__main__":
    node5 = Node(5)
    node4 = Node(4,node5)
    node3 = Node(3,node4)
    node2 = Node(2,node3)
    node1 = Node(1,node2)

    tour(node1)