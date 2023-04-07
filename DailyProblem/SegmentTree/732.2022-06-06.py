from collections import defaultdict
'''
732. 我的日程安排表 III
https://leetcode.cn/problems/my-calendar-iii/

线段树
隐约记得去年蓝桥杯国赛考到了类似的题，实习笔试也做到了类似的题，复习复习。
节省空间复杂度，动态开点。
tree代表每个节点区间的最终结果
lazy记录正好覆盖这个区间的值
所以tree当前节点的值更新为：左子节点的结果 + 右子节点的结果 + 当前节点的值
时间复杂度O(nlogC)，空间复杂度为O(nlogC)，n为查询次数，C为动态开点范围。
'''
class MyCalendarThree:

    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start, end, l, r, index):
        if end < l or start > r:
            return
        if start <= l and end >= r:
            self.tree[index] += 1
            self.lazy[index] += 1
            return
        
        mid = l + (r - l) // 2
        self.update(start, end, l, mid, 2 * index)
        self.update(start, end, mid + 1, r, 2 * index + 1)
        self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1]) + self.lazy[index]


    def book(self, startTime: int, endTime: int) -> int:
        self.update(startTime, endTime - 1, 0, 10**9, 1)
        return self.tree[1]

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)

s = MyCalendarThree()
ops = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
res = [0] * len(ops)
for i, (st, ed) in enumerate(ops):
    res[i] = s.book(st, ed)
print(res)