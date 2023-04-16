'''
2023-04-15 算法岗 3

题目描述：
游游拿到了一棵树，共有n个节点。每个节点都有一个权值：0或者1。
这样,每条路径就代表了一个二进制数。游游想知道,有多
少条路径代表的二进制数在[l,r]区间范围内？
(请注意:路径长度至少为1，例如，节点3到节点3虽然有一个权值，但并不是合法路径！)

输入描述
第一行输入三个正整数n,l,r，用空格隔开。
第二行输入一个长度为n的01串，第i个字符代表号节点的权值。
接下来的n - 1行,每行输入两个正整数u和v，代表u号节点和v号节点有一条边连接。
1<=n<=10^3
1<=u,v<=n
1<=l<=r<=10^14

输出描述
一个整数，代表合法的路径条数。

输入示例
4 4 5 
1010
1 2
2 3
3 4

输出示例
3
'''
# 思路
'''
这个数据范围，直接搜就行。
时间复杂度O(n^2)
'''
line1 = input().strip().split(' ')
n, l, r = int(line1[0]), int(line1[1]), int(line1[2])
string = input().strip()
g = [set() for _ in range(n)]
for _ in range(n - 1):
    line2 = input().strip().split(' ')
    u, v = int(line2[0]), int(line2[1])
    g[u - 1].add(v - 1)
    g[v - 1].add(u - 1)
res = 0

def dfs(index, s):
    global res
    seen.add(index)
    num = int(s + string[index], 2)
    if num <= r and num >= l and len(s) >= 1:
        res += 1
    elif num > r:
        return
    for num in g[index]:
        if num not in seen:
            
            dfs(num, s + string[index])
    seen.remove(index)
for i in range(n):
    seen = set()
    dfs(i, "")
print(res)