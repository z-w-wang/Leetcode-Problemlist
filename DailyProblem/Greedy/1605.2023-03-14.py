from typing import List
'''
1605. 给定行和列的和求可行矩阵
https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/

贪心
从0, 0开始，每次尽量满足一行或者一列的和
即每次对于行和和列和 选择最小的数作为i, j位置的值 较大的数减去最小的数 和下一行或者下一列的进行比较
'''
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]
        while i < m and j < n:
            if rowSum[i] > colSum[j]:
                res[i][j] = colSum[j]
                rowSum[i] -= colSum[j]
                j += 1
            else:
                res[i][j] = rowSum[i]
                colSum[j] -= rowSum[i]
                i += 1
        return res


s = Solution()
print(s.restoreMatrix([5, 7, 10], [8, 6, 8]))
