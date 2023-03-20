'''
2023-03-19 NLP算法方向 2

题目描述：
米小游希望你构造一个长度为n的数组，满足以下条件：
1.所有元素的绝对值不大于3.
2.相邻两个元素的乘积小于0，且和不为0。
3.所有元素之和等于0。
你能帮帮她妈？

输入描述：
一个正整数n。
2<=n<=100000

输出描述：
如果无解，请输出一个字符串"No Answer"。
否则输出n个整数。有多解输出任意即可。
'''
# 思路
'''
纯归纳构造。
'''

# 未测试
n = int(input())

if n == 1 or n == 2:
    print("No Answer")

else:
    res = [0] * n
    iter_num = n
    if n % 4 == 1:
        iter_num -= 5
        res[-5: ] = [-1, 3, -1, 2, -3]
    if n % 4 == 2:
        iter_num -= 6
        res[-6: ] = [-2, 3, -1, 2, -3, -1]
    if n % 4 == 3:
        iter_num -= 3
        res[-3: ] = [-1, 2, -1]
    for i in range(iter_num):
        if i % 4 == 0:
            res[i] = 2
        elif i % 4 == 1:
            res[i] = -1
        elif i % 4 == 2:
            res[i] = 2
        else:
            res[i] = -3
for num in res:
    print(num, end=' ')