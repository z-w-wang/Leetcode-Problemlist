from typing import Optional, List
from collections import deque
'''
1026. 节点与其祖先之间的最大差值
https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/

DFS
记录每个节点的子树的最大值和最小值，并用该节点与其子树的最大值最小值比较。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if node is None:
                return 10 ** 5, 0
            nonlocal res
            minleft, maxleft = dfs(node.left)
            minright, maxright = dfs(node.right)
            res = max(res, node.val - min(minleft, minright), max(maxleft, maxright) - node.val)
            return min(minleft, minright, node.val), max(maxleft, maxright, node.val)
        
        dfs(root)
        return res


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

tree = [8,3,10,1,6,None,14,None,None,4,7,13]
root = init_binarytree(tree)
s = Solution()
print(s.maxAncestorDiff(root))