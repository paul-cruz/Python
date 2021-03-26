class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearhTree:
    def __init__(self):
        self.root = None

    def empty(self) -> bool:
        return self.root is None
    
    def search(self, value: int) -> bool:
        return self.helper_search(self.root, value) is not None
    
    def helper_search(self, node: Node, value: int) -> Node:
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self.helper_search(node.left, value)
        else:
            return self.helper_search(node.right, value)

    def insert(self, new_value: int) -> None:
        if self.empty():
            self.root = Node(new_value)
        self.helper_insert(self.root, new_value)

    def helper_insert(self, node: Node, new_value: int) -> None:
        if new_value < node.value:
            if node.left is None:
                node.left = Node(new_value)
            else:
                self.helper_insert(node.left, new_value)
        elif new_value > node.value:
            if node.right is None:
                node.right = Node(new_value)
            else:
                self.helper_insert(node.right, new_value)

    def bfs_iterative(self) -> None:
        if self.root is None:
            return

        queue = []
        queue.append(self.root)
        level = 1

        while(queue):
            level_nodes = len(queue)
            print('Level {}: '.format(level), end=' ')
            while level_nodes > 0:
                node = queue.pop(0)
                print(node.value, end=' ')

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                level_nodes -= 1
            level += 1
            print('')

if __name__ == "__main__":
    tree = BinarySearhTree()

    tree.insert(9)  #     9
    tree.insert(8)  #   /   \
    tree.insert(5)  #  8    10
    tree.insert(10) # /      \
    tree.insert(6)  # 5      15
    tree.insert(15) # \      /
    tree.insert(13) # 6     13

    print("BFS traversal iterative:")
    tree.bfs_iterative()
    print(tree.search(9))
    print(tree.search(8))
    print(tree.search(5))
    print(tree.search(10))
    print(tree.search(6))
    print(tree.search(15))
    print(tree.search(13))
    print(tree.search(0))
    print(tree.search(100))
    print(tree.search(3))

