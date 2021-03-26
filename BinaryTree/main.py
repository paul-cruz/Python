class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs_traversal(root):
    q = list()
    q.append(root)
    helper_bfs(q)
    print('')


def helper_bfs(q):
    node = None
    if len(q) > 0:
        node = q.pop(0)
    if node is None:
        return
    print(node.value, end=' ')
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)
    helper_bfs(q)

def bfs_iterative(root):
    if root is None:
        return

    queue = []
    queue.append(root)
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
    #root = Node(10)                                     #       10   
    #root.left = Node(11)                                #      / \
    #root.left.left = Node(7)                            #     11  9
    #root.right = Node(9)                                #    /   / \
    #root.right.left = Node(15)                          #   7   15  8
    #root.right.right = Node(8)

    root = Node(9)                                      #               9
    root.left = Node(8)                                 #              /
                                                        #             8
    root.left.left = Node(5)                            #            / \
                                                        #           5  10
    root.left.right = Node(10)                          #           \  /
                                                        #           5  6
    root.left.right.left = Node(6)                      #          /
                                                        #         6
    root.left.left.right = Node(5)                      #
    root.left.left.right.left = Node(6)                 #

    print("BFS traversal recursive:", end = " ") 
    bfs_traversal(root)

    print("BFS traversal iterative:") 
    bfs_iterative(root)
