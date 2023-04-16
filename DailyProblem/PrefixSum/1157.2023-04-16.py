from typing import List
from collections import defaultdict
from bisect import bisect_left
'''
1157. 子数组中占绝大多数的元素
https://leetcode.cn/problems/online-majority-element-in-subarray/

数位+前缀和+二分查找
统计每个数字的下标和其数位的出现次数前缀和
区间数位出现次数大于阈值的可能为多数元素，利用二分查找判断区间内该数个数，即为结果。
特别地，如果区间数位出现次数小于阈值，那么多数元素在该位的取值可能为0，如果0的个数小于阈值可直接return -1
官解方法懒得看。
时间复杂度：初始化O(nL)，每个查询O(L + logn)，其中n为arr数组长度，L为arr数组中最大值的二进制位数，题目样例中L<=15。
'''
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.n = len(bin(max(arr))) - 2
        self.prefixs = [[0] * self.n for _ in range(len(arr) + 1)]
        self.indexs = defaultdict(list)
        for i, num in enumerate(arr):
            if num in self.indexs:
                self.indexs[num].append(i)
            else:
                self.indexs[num] = [i]
            bit1 = bin(num)[2:]
            for j in range(len(bit1)):
                self.prefixs[i + 1][j] = self.prefixs[i][j]
                if bit1[len(bit1) - 1 - j] == '1':
                    self.prefixs[i + 1][j] += 1
            for j in range(len(bit1), self.n):
                self.prefixs[i + 1][j] = self.prefixs[i][j]
        
    def query(self, left: int, right: int, threshold: int) -> int:
        res = 0
        for i in range(self.n - 1, -1, -1):
            res *= 2
            if self.prefixs[right + 1][i] - self.prefixs[left][i] >= threshold:
                res += 1
            elif right + 1 - left  - self.prefixs[right + 1][i] + self.prefixs[left][i] < threshold:
                return -1  
        if bisect_left(self.indexs[res], right + 1) - bisect_left(self.indexs[res], left) < threshold:
            return -1
        return res

s = MajorityChecker([1, 1, 2, 2, 1, 1])
queries = [[0, 5, 4], [0, 3, 3], [2, 3, 2]]
res = [0] * len(queries)
for i, q in enumerate(queries):
    res[i] = s.query(*q)
print(res)