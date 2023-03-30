'''
2023-03-30 3.游游的数值距离

时间限制：C/C++ 1秒，其他语言 2秒
空间限制：C/C++ 262144K，其他语言 524288K

题目描述:
游游拿到了一个正整数n，她希望找到一对正整数x,y，满足|x! × y - y - n|最小，且x,y都不等于2，感叹号表示阶乘。你能帮帮她吗?

输入描述：
一个正整数n
1<=n<=10^9

输出描述：
输出两个正整数，分别表示x,y。
如果有多解，输出任意一解即可通过.

样例输入：
2

样例输出：
1 1
'''
# 思路
'''
首先根据范围，因为12!大于4*10^9，所以x的取值范围缩小到[1,11]。
然后根据 y = n // (x! - 1) 确定y的值
要比较y和y+1，因为取整问题。
时间复杂度:O(1)
'''
n = int(input())
min_minus = n
x1, y1 = 1, 1
huge = 2
for x in range(3, 12):
    huge *= x
    if huge > 2 * n:
        break
    left = huge - 1
    y = n // left
    minus = abs(n - y * left)
    if y > 0 and y != 2 and minus < min_minus:
        min_minus = minus
        x1, y1 = x, y
    minus = abs(n - y * left - left)
    if y != 1 and minus < min_minus:
        min_minus = minus
        x1, y1 = x, y + 1
print(x1, y1)