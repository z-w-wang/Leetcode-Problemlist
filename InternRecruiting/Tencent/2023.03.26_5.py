'''
2023-03-26 算法岗 5
时间限制：C/C++ 1秒，其他语言2秒。
空间限制：C/C++ 262144K，其他语言 524288K。
题目描述：
木匠牛牛现在拿到了一块长度为W，高度为H的矩形木板，为了方便切割木板，牛牛要对这个木板画m条标记线。
牛牛先把整块木板放到一个笛卡尔坐标系中，木板的左下角的坐标为(0,0)，左上角的坐标为(0,H)，右下角的坐标为，右上角的座标为。
对于第i条标记线的画法为：选择两个整数坐标点(xi1,yi1)，(xi2,yi2)，画一条经过两点的直线。
为了保证木板切割的美观程度:牛牛所绘制的标记线的斜率只可能是-1或1（即只能斜着切）。
绘制完所有的标记线之后，牛牛用锯子沿着每条标记线进行切割，切割完之后会得到很多小木板。
牛牛想知道切割完后小木板的个数是多少。
输入描述：
第一行输入两个正整数H,W表示木板的高度和长度。
第二行输入一个正整数m表示标记线的条数。
接下来 m 行每行四个正整数xi1,yi1,xi2,yi2表示标记线经过的坐标点
(1<H,W<500，1<=m<=1000，0<=xi1,xi2<=W，0<=yi1,yi2<=H。
数据保证(xi1,yi1)≠(xi2,yi2)。
注:如果某条线段出现了多次，按照一次统计即可。
输出描述：
输出小木板的条数。
'''
# 100%
line1 = input().strip().split(' ')
h, w = int(line1[0]), int(line1[1])
m = int(input())
# 斜率为1的放在s1，斜率为2的放在s2。
s1 = set()
s2 = set()
for _ in range(m):
    line1 = input().strip().split(' ')
    x1, y1, x2, y2 = int(line1[0]), int(line1[1]), int(line1[2]), int(line1[3])
    k = (y2 - y1) // (x2 - x1)
    b = y1 - x1 if k == 1 else y1 + x1
    # 判断该直线是否切到了木板，没切到的不要。
    if k == 1 and (b >= h or b <= -w) or k == -1 and (b >= h + w or b <= 0):
        continue
    if k == 1:
        s1.add(b)
    else:
        s2.add(b)

len1 = len(s1)
# res初始化为计算斜率为1的线能切出的块数
res = len1 + 1
# 计算每一条斜率为-1的线能多切出来的块数：与斜率为1的线的交点中，交点在木板内的交点个数+1
for b2 in s2:
    count = len1 + 1
    for b1 in s1:
        if b1 >= b2 or b1 + b2 >= 2 * h or b1 + b2 <= 0 or b2 - b1 >= 2 * w:
            count -= 1
    res += count
print(res)