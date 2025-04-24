class TreeNode:
    '''
    In-order traversal give sorted form for the binary search
                    5
                   /| \
                  4 | 6
                  | | |
                  4 5 6
    '''
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def inorder_iterative(root):
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            # do stuff here
            root = stack.pop()
            root = root.right

def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        # do something here
        inorder_recursive(root.right)