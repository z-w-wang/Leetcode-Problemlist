'''
2023-03-26 算法岗 3
时间限制：C/C++ 1秒，其他语言2秒。
空间限制：C/C++ 262144K，其他语言 524288K。
题目描述：
KL散度是机器学习，深度学习等领域中关于分布距离度量的重要的方法。
对于两个给定连续分布P和Q，他们的KL散度定义为DKL(p||q)=∫ p(x)log(p(x)/q(x)) dx。
对于两个正态分布N(μp,Σp)和N(μq,Σq)，可以通过简单的运算得知他们的KL散度为
DKL(p||q)=[log|Σp/Σq| - k + (μp - μq)T Σq(-1) (μp - μq) + tr{Σq(-1) Σp}],
其中|·|表示行列式，(·)T表示转置，(·)(-1)表示逆矩阵，tr(·)表示矩阵对角线元素求和，log以自然对数e为底。
现在给定其中一个正态分布q为N(0, I)，另一个分布p为N(0,Σp')。Σp'是一个k阶对角阵，
试判断这两个正态分布的KL散度DKL(p||q)是否大于给定阈值t，若大于则输出1，否则输出0.
输入描述：
第一行表示为测试数据组数T，接下来每一组有两行，
一组的第一行为k和t，矩阵Σp'的维度为k×k，t为给定阈值。其中1<=k<=1000，1<=t<=100000。
一组的第二行有k个浮点数，为矩阵Σp'的对角元。
'''
# 思路
'''
把数据带入公式，化简成(tr(Σp) - k - log|Σp|)/2，再模拟就行。
'''

# 100%
import math
t = int(input().strip())
res = [0] * t

for i in range(t):
    line1 = input().strip().split(' ')
    k, t = float(line1[0]), float(line1[1])
    diag = list(map(float, input().strip().split(' ')))
    mult = 1
    for d in diag:
        mult *= d
    kl = (-math.log(mult) - k + sum(diag)) / 2
    if kl > t:
        res[i] = 1

for r in res:
    print(r)