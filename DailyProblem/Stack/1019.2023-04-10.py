from typing import Optional, List
'''
1019. 链表中的下一个更大节点
https://leetcode.cn/problems/next-greater-node-in-linked-list/

单调栈
按照题目要求模拟就行
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        def nodeiter(node):
            while node:
                yield node.val
                node = node.next

        nodelist = [x for x in nodeiter(head)]
        stack = []
        res = [0] * len(nodelist)
        for i, num in enumerate(nodelist):
            while len(stack) > 0 and stack[-1][0] < num:
                res[stack[-1][1]] = num
                stack.pop()
                
            stack.append([num, i])
        return res
    
list1 = [2,7,4,3,5]
head = ListNode()
cur = head
for num in list1:
    cur.next = ListNode(num)
head = head.next
s = Solution()
print(s.nextLargerNodes(head))