from LinkedList import LinkedList

if __name__ == "__main__":
    llist = LinkedList()

    for i in range(1,5):
        llist.add(i)
    
    print('Original List: ')
    llist.print_list()
    llist.insert(0)
    print('List after insert: ')
    llist.print_list()
    llist.remove()
    print('List after remove: ')
    llist.print_list()
    llist.pop()
    print('List after pop: ')
    llist.print_list()
    print(llist.locate(2))
    print(llist.locate(100))
    print(llist.search(3))
    print(llist.search(10))
    llist.clear_out()
    print('empty list: ')
    llist.print_list()