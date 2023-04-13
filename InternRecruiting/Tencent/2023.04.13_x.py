'''
2023-04-13
题目描述：
小红定义一个数组为“好数组”，当且仅当该数组满足以下条件：
1.数组仅由0,1,2三种元素组成。
2.整数相邻的元素不相等。
例如[2,1,2,0,1]是好数组
小红定义一个数组的“陡峭值”为该数组相邻元素的差的绝对值之和。
小红想知道，长度为n的所有好数组的陡峭值之和是多少？
输出答案对10^9+7取模。

输入描述：
一个整数n，2<=n<=10^9
输出描述：
一个数，输出陡峭值之和
'''
# 思路
'''
对于每个n，其末尾为0,1,2的好数组个数相等，均为2^(n-1)个。
于是n都只与其n-1时的好数组情况有关。
设dp[i][x]代表好数组长度为i时，最后一个数为x的好数组的陡峭值之和，base[i]=2^(i - 2)，有：
dp[i][0] = (dp[i - 1][1] + 1 * base[i]) + (dp[i - 1][2] + 2 * base[i])
dp[i][1] = (dp[i - 1][0] + 1 * base[i]) + (dp[i - 1][2] + 1 * base[i])
dp[i][2] = (dp[i - 1][0] + 2 * base[i]) + (dp[i - 1][1] + 1 * base[i])
时间复杂度为O(n)，由于n的取值最大为10^9，dp会超时，所以继续优化。

设s[i] = sum(dp[i])
则s[i] = 2 * s[i - 1] + 2 ^ (i + 1)
变形得：
s[i] - i * 2^(i + 1) = 2 * (s[i - 1] + (i - 1) * 2^i)
为公比为2的等比数列
化简得s[n] = (n - 1) * 2^(n + 1)
时间复杂度为O(1)

对于取模操作，s[n]数可能特别大，最后再取模可能溢出。
可以用快速幂。
设mod = 10**9+7
res = ((n - 1) % mod) * (2^(n+1) % mod)
设p[n] = 2^n % mod
则p[n] = (p[n // 2] * p[n // 2]) % mod if n & 1 == 0
       = (p[n // 2] * p[n // 2] * 2) % mod if n & 1 == 1

时间复杂度为O(logn)
'''
n = int(input())
res = (n - 1) * 2^(n + 1)
print(res % (10**9+7))