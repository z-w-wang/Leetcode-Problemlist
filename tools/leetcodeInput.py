from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def init_binarytree(tree: List[int]) -> Optional[TreeNode]:
    root = TreeNode(tree[0])
    q = deque([root])
    p = 1
    while q and p < len(tree):
        node = q.popleft()
        if tree[p]:
            node.left = TreeNode(tree[p])
            q.append(node.left)
        if p + 1 < len(tree) and tree[p + 1]:
            node.right = TreeNode(tree[p + 1])
            q.append(node.right)
        p += 2
    return root