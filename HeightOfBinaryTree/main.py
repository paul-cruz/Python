class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def get_height(root):
    if root is None:
        return 0

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return(max(left_height,right_height)+1)

if __name__ == "__main__":
    r"""root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5)"""
    
    root = Node(10)                                     #       10   
    root.left = Node(11)                                #      / \
    root.left.left = Node(7)                            #     11  9
    root.right = Node(9)                                #    /   / \
    root.right.left = Node(15)                          #   7   15  8
    root.right.right = Node(8)

    
    r"""root = Node(9)                                      #               9
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
    """
    print ("The height of the BT is %d" %(get_height(root))) 