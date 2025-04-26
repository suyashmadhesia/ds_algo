class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    initution is to go left of the tree if a find any value which is equal to p or q just return the current root
    else if left is null then we have to check the write part so we return right (even if it is null)
    else if right is null then we have to check the left part so we return left (even if it is null)
    and if both have some value then it means nodes are into the give root of the tree at that moment 
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if not root or p == root or q == root:
                return root
            left = dfs(root.left, p, q)
            right =dfs(root.right, p, q)

            if not left:
                return right

            elif not right:
                return left
            
            else:return root

        return dfs(root, p, q)
        