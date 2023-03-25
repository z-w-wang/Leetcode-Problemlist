'''
2023-03-25 算法岗 3.春游
时间限制： 3000MS
内存限制： 589824KB
题目描述：
小美明天要去春游了。她非常喜欢吃巧克力，希望能够带尽可能多的巧克力在春游的路上吃。
她现在有n个巧克力，很巧的是她所有的巧克力都是厚度一样的正方形的巧克力板，这n个巧克力板的边长分别为a1,a2,...,an。
因为都是厚度一致的正方形巧克力板，我们认为第 i 个巧克力的重量为。
小美现在准备挑选一个合适大小的包来装尽可能多的巧克力板，她十分需要你的帮助来在明天之前准备完成，请你帮帮她。

输入描述
第一行两个整数n和m，表示小美的巧克力数量和小美的询问数量。
第二行n个整数a1,a2,...,an，表示n块正方形巧克力板的边长。注意你不能将巧克力板进行拆分。
第三行m个整数q1,q2,...,qm，第 i 个整数qi表示询问：如果小美选择一个能装qi重量的包，最多能装多少块巧克力板？
（不考虑体积影响，我们认为只要质量满足要求，巧克力板总能塞进包里）
1≤n,m≤50000,1≤ai≤104,1≤qi≤1018

输出描述
输出一行m个整数，分别表示每次询问的答案。

样例输入
5 5
1 2 2 4 5
1 3 7 9 15
样例输出
1 1 2 3 3
'''
# 思路
'''
贪心+前缀和+二分查找
为了拿到更多的巧克力，每次从小的先拿，所以先排序
然后前缀和，去掉每次重复的从小往大加
搜的时候用二分查找
时间复杂度O((n + q)logn)，排序O(nlogn)，前缀和数组O(n)，查询O(qlogn)
其中n为巧克力块数，q为查询数。
'''
# 100%
from bisect import bisect_right
line1 = input().split(" ")
n, m = int(line1[0]), int(line1[1])
line2 = input().split(" ")
borders = list(map(int, line2))
line3 = input().split(" ")
queries = list(map(int, line3))

borders.sort()
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + borders[i] * borders[i]
res = [0] * m
prefix.pop(0)
for i, query in enumerate(queries):
    res[i] = bisect_right(prefix, query)

for r in res:
    print(r, end=' ')