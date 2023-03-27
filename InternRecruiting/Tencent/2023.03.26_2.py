'''
2023-03-26 算法岗 2
时间限制：C/C++ 1秒，其他语言2秒。
空间限制：C/C++ 262144K，其他语言 524288K。
题目描述：
又到了收割韭菜的季节，根据历史的经验，为了让韭菜更肥更壮，要让韭菜长到一定的合适的长度。
众所周知，嫩韭菜太短而收获不多，老韭菜口味不佳。所以大型的机构都要估计韭菜的大概长度，开年来一波机械化收割。
假设一批非菜的平均长度服从密度函数为sin(sqrt(x))/5.68的分布，其中平均长度x介于[1,10]之间。
机构想知道介于[a,b]⊂[1,10]的的概率是否大于0.5以方便收割最大化。
我们知道通过数值积分可以给出：P(a<=X<=b)=∫(a→b) sin(sqrt(x))/5.68 dx ≈ Σ(i=0→n-1) sin(sqrt(x))/5.68 Δx
其中a=x0<x1<...<xn=b，and x(i+1)-xi = Δx。取n=500，相当于把区间[a,b]分成500份。
输入描述：
第一行表示测试数据组数T。
接下来的T行，每一行表示输入a、b，1<=a<b<=10。
输出描述
输出1或者0，如果得到的概率大于0.5则输出1否则则输出0。
'''
# 100%
import math
t = int(input().strip())
res = [0] * t
for i in range(t):
    line = input().strip().split(' ')
    a, b = int(line[0]), int(line[1])
    range1 = (b - a) / 500
    prob = 0.0
    for j in range(500):
        left = j * range1
        prob += math.sin(math.sqrt(left + range1/2)) * range1 / 5.68
    if prob > 0.5:
        res[i] = 1
for r in res:
    print(r)