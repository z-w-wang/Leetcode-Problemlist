from typing import Optional
'''
1373. 二叉搜索子树的最大键值和

dfs
边统计和边判断是否为搜索树即可。
一旦子树不为搜索树，直接520520。
'''
null = None
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return 0, 520520, -520520
            sum_left, min_left, max_left = dfs(node.left)
            sum_right, min_right, max_right = dfs(node.right)
            if min_left == -520520 or min_right == -520520 or max_left == 520520 or max_right == 520520:
                return 0, -520520, 520520
            if max_left >= node.val or min_right <= node.val:
                return 0, -520520, 520520
            sum1 = sum_left + sum_right + node.val
            res = max(res, sum1)
            return sum1, min(node.val, min_left), max(node.val, max_right)
        _, _, _ = dfs(root)
        return res

s = Solution()
print(s.maxSumBST([1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]))