from heapq import heappush, heappop
'''
1172. 餐盘栈
https://leetcode.cn/problems/dinner-plate-stacks/

堆
stack数组纯模拟，用popped记录未满的stack[i]
时间复杂度O(nlogn)，n为查询次数
'''
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.popped = []

    def push(self, val: int) -> None:
        if self.popped and self.popped[0] >= len(self.stack):
            self.popped = []
        if len(self.popped) == 0:
            self.stack.append([val])
            if self.capacity > 1:
                heappush(self.popped, len(self.stack) - 1)
            return
        self.stack[self.popped[0]].append(val)
        if len(self.stack[self.popped[0]]) == self.capacity:
            heappop(self.popped)
        
    def pop(self) -> int: 
        return self.popAtStack(len(self.stack) - 1)

    def popAtStack(self, index: int) -> int:
        if not self.stack or index >= len(self.stack) or len(self.stack[index]) == 0:
            return -1
        if len(self.stack[index]) == self.capacity:
            heappush(self.popped, index)
        res = self.stack[index].pop()
        while self.stack and len(self.stack[-1]) == 0:
            self.stack.pop()
        return res