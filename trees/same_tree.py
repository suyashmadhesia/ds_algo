"""
Function to find if a tree is same to another tree structure and value wise
"""

from typing import Optional


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not q and not p:
        return True

    if p and not q or q and not p:
        return False

    if p.val != q.val or p.val != q.val:
        return False

    left = isSameTree(p.left, q.left) 
    right = isSameTree(p.right, q.right)

    return left and right
