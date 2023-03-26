'''
2023-03-26 测试岗 3.涂色

时间限制:3000MS
内存限制:589824KB

题目描述:
给出一个数组。你需要求出按顺序对其进行一系列区间操作后最终所得的数组。
操作有三种:
1.将下标在L到R之间的元素全部或上X。
2.将下标在L到R之间的元素全部与上X。
3.将下标在L到R之间的元素全部设为X。

输入描述：
第一行有一个正整数N(1<=N<=100000)，代表数组的长度。
第二行有N个非负整数，范围在0到2^20-1之间，代表数组中的元素。
第三行有一个正整数M(1<=M<=100000)，代表操作次数。
第四行有M个正整数，代表M次操作中的区间左端点L。
第五行有M个正整数，代表M次操作中的区间右端点R。
第六行是一个长度为M的字符串，'|'代表操作1，'&'代表操作2 ，'='代表操作3。
第七行有M个正整数，代表M次操作中的参数X。

输出描述：
在一行中输出N个数，代表所有操作按顺序完成后最终所得的数组。

样例输入：
4
5 4 7 4
4
1 2 3 2
4 3 4 2
=|&=
8 3 6 2
样例输出
8 2 2 0
'''
# 思路
'''
直接暴力模拟能过82%

感觉可以用线段树记录操作，每个节点开一个20长度的记录数组 和一个标记数字。
遇到与就在0对应位置上置0，遇到或就在1对应位置上置1，有等于号操作，清空记录数组，标记数字为等于的数字。
然后再遍历这个线段树，从根到叶子结点记录操作，最后有0或者1的赋值，其他二进制位置用原来数字的。
时间复杂度O((n+c)logn)
'''
# 未完成
from collections import defaultdict

n = int(input().strip())
nums = list(map(int, input().strip().split(' ')))
m = int(input().strip())
Ls = list(map(int, input().strip().split(' ')))
Rs = list(map(int, input().strip().split(' ')))
ops = input().strip()
attrs = list(map(int, input().strip().split(' ')))

class Tree:
    def __init__(self):
        self.tree = defaultdict([-1] * 21)

    def update(self, start: int, end: int, l: int, r: int, idx: int, op: str, num: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            if op == '&':
                for i in range(20):
                    if num == 0:
                        break
                    else:
                        if num & 1 == 0:
                            self.tree[idx][i] = 0
                        num = num >> 1
            elif op == '|':
                for i in range(20):
                    if num == 0:
                        break
                    else:
                        if num & 1:
                            self.tree[idx][i] = 1
                        num = num >> 1
            else:
                for i in range(20):
                    self.tree[idx][i] = -1
                self.tree[-1] = num

        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, idx * 2)
            self.update(start, end, mid + 1, r, idx * 2 + 1)

    
t = Tree()
for i in range(m):
    t.update(Ls[i] - 1, Rs[i] - 1, 0, n, 1, ops[i], attrs[i])

