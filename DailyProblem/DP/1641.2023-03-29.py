'''
1641. 统计字典序元音字符串的数目
https://leetcode.cn/problems/count-sorted-vowel-strings/

动态规划
用dp[i] = [num_a, num_e, num_i, num_o, num_u]代表长度为i的、末尾为aeiou的各自的数量。
显然有dp[i][j] = sum(dp[i - 1][: j])
即dp[i]是dp[i - 1]的前缀和数组。

代码：
class Solution:
    def countVowelStrings(self, n: int) -> int:       
        ends = [1, 1, 1, 1, 1]
        for _ in range(n - 1):
            for i in range(1, 5):
                ends[i] += ends[i - 1]
        return sum(ends)

时间复杂度为O(Σn)，空间复杂度为O(Σ)，本题Σ=5。

可以用矩阵快速幂简化时间复杂度，有：
d(i) = Md(i-1)，d(i)为长度为i时的列向量dp。
M=[[1, 0, 0, 0, 0], 
[1, 1, 0, 0, 0], 
[1, 1, 1, 0, 0], 
[1, 1, 1, 1, 0], 
[1, 1, 1, 1, 1]]

时间复杂度为O(Σ^3 logn)，空间复杂度为O(Σ^2 n)

官解有用组合数做的，时间复杂度为O(1)
'''
    

class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        matrix = [[1, 0, 0, 0, 0], 
                [1, 1, 0, 0, 0], 
                [1, 1, 1, 0, 0], 
                [1, 1, 1, 1, 0], 
                [1, 1, 1, 1, 1]]

        def mat_pow(matrix1, n):
            if n == 1:
                return matrix1
            matrix2 = mat_pow(matrix1, n // 2)
            res_mat = mat_mul(matrix2, matrix2)
            if n % 2:
                res_mat = mat_mul(res_mat, matrix)

            return res_mat

        def mat_mul(matrix1, matrix2):
            res_mat = [[0] * 5 for _ in range(5)]
            for i in range(5):
                for j in range(5):
                    for k in range(5):
                        res_mat[i][j] += matrix1[i][k] * matrix2[k][j]
            return res_mat
        
        mat = mat_pow(matrix, n - 1)
        return sum(sum(m) for m in mat)
    
s = Solution()
print(s.countVowelStrings(6))