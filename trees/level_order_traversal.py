from typing import Optional, List

from collections import deque

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    '''
    This level order traversal
    '''
    if not root:
        return []
    q = deque()
    q.append([root])
    finalRes = []
    while q:
        nodes = q.popleft()
        res = []
        layerNode = []
        for node in nodes:
            if node.left: layerNode.append(node.left)
            if node.right: layerNode.append(node.right)
            res.append(node.val)
        
        if res:
            finalRes.append(res)
        if layerNode:
            q.append(layerNode)
    return finalRes

        