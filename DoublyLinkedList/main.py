from DoublyLinkedList import DoublyLinkedList

if __name__ == "__main__":
    dll = DoublyLinkedList()

    for i in range(1,10):
        dll.add(i)

    dll.insert(0)

    print('Order List: ')
    dll.print()
    print('Reverse Order List: ')
    dll.rprint()

    print('Size : ' + str(dll.get_size()))
    dll.pop()
    print('List: ')
    dll.print()
    print('Size : ' + str(dll.get_size()))
    dll.remove()
    print('List: ')
    dll.print()
    print('Size : ' + str(dll.get_size()))