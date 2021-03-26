from typing import Tuple

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced( root: Node) -> bool:
        def dfs_balanced(root: Node) -> Tuple[int,bool]:
            if root is None:
                return 0,True

            left_height, bal_left = dfs_balanced(root.left)
            right_height, bal_right = dfs_balanced(root.right)
            
            bal = True if bal_left and bal_right and (-1 <= left_height - right_height <= 1) else False
            
            return (max(left_height,right_height)+1), bal
        return dfs_balanced(root)[1]

if __name__ == "__main__":
    root = Node(1)                                      #          1
    root.left = Node(2)                                 #         / \
    root.right = Node(3)                                #        2  3
    root.left.left = Node(4)                            #       / \
    root.left.right = Node(5)                           #      4   5
    
    r"""root = Node(10)                                     #       10   
    root.left = Node(11)                                #      / \
    root.left.left = Node(7)                            #     11  9
    root.right = Node(9)                                #    /   / \
    root.right.left = Node(15)                          #   7   15  8
    root.right.right = Node(8)"""

    
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
    root.left.left.right.left = Node(6)                 #"""
    
    print ("The BT is%sbalanced" %(" " if is_balanced(root) == True else " not ")) 
