from typing import List
'''
剑指 Offer II 107. 矩阵中的距离 == 542

广度遍历搜索求最短路径
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        que = []
        res = [[0] * n for _ in range(m)]

        # 找出所有最贴近0的1
        for i, ma in enumerate(mat):
            for j, val in enumerate(ma):
                if val == 1:
                    for p, q in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),):
                        if 0 <= p < m and 0 <= q < n and mat[p][q] == 0:                           
                            que.append((i, j,))
                            res[i][j] = 1
                            break
        
        # 从1的边缘开始广度搜索                       
        flag = 2
        while que:
            tempq = []
            for i, j in que:
                for p, q in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),):
                    if 0 <= p < m and 0 <= q < n and mat[p][q] == 1 and res[p][q] == 0:
                        tempq.append((p, q,))
                        mat[p][q] = 0
                        res[p][q] = flag
            flag += 1
            que = tempq[:]
        return res
    
s = Solution()
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))