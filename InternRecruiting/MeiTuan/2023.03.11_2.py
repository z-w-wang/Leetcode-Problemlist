'''
测试岗2023-03-11 2.流星

时间限制：3000 MS
内存限制：589824 KB

题目描述：
小美是一位天文爱好者，她收集了接下来一段时间中所有会划过她所在的观测地上空的流星信息。
具体地，她收集了n个流星在她所在观测地上空的出现时刻和消失时刻。
对于一个流星，若其的出现时刻为s，消失时刻为t，那么小美在时间段[s,t]都能够观测到它。
对于一个时刻，观测地上空出现的流星数量越多，则小美认为该时刻越好。
小美希望能够选择一个最佳的时刻进行观测和摄影，使她能观测到最多数量的流星。
现在小美想知道，在这个最佳时刻，她最多能观测到多少个流星以及一共有多少个最佳时刻可供她选择。

输入描述：
第一行是一个正整数n，表示流星的数量。
第二行是n个用空格隔开的正整数，第i个数si表示第i个流星的出现时间。
第三行是n个用空格隔开的正整数，第i个数ti表示第i个流星的消失时间。
1<=n<=100000, 1<=si<=ti<=10^9

输出描述：
输出一行用空格隔开的两个数x和y，其中x表示小美能观测到的最多流星数，y表示可供她选择的最佳时刻数量。

样例输入：
3
2 1 5
6 3 7

样例输出：
2 4
'''
# 思路
'''
区间和问题，线段树。
由于数据范围在1到10^9，所以动态开点。
用lazy标记节省update时间。
查询个数时，搜索满足数量最多的最小区间，相加即可。
不知道样例通过情况。
'''
from collections import defaultdict
starnum = int(input())
line2 = input().split(' ')
line3 = input().split(' ')

appeartimes = [int(time) for time in line2]
disappeartimes = [int(time) for time in line3]


class Tree:
    def __init__(self):
        self.tree = defaultdict(int)
        self.res = 0
        self.lazy = defaultdict(int)

    def update(self, start, end, l, r, idx):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, idx * 2)
            self.update(start, end, mid + 1, r, idx * 2 + 1)
            self.tree[idx] = self.lazy[idx] + \
                max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def search(self, l, r, idx, target):
        if self.tree[idx] < target or target == 0:
            return False

        mid = l + (r - l) // 2
        left = self.search(l, mid, idx * 2, target - self.lazy[idx])
        right = self.search(mid + 1, r, idx * 2 + 1, target - self.lazy[idx])

        if not left and not right:
            self.res += r - l + 1
            return True

        return left or right


t = Tree()

for (start, end) in zip(appeartimes, disappeartimes):
    t.update(start, end, 0, 10 ** 9, 1)

t.search(0, 10 ** 9, 1, t.tree[1])

print(t.tree[1], t.res)
