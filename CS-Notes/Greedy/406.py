from typing import List
'''
406. 根据身高重建队列
https://leetcode.cn/problems/queue-reconstruction-by-height/

贪心算法。
因为每个人的相对位置只取决于比他高的人的位置，所以先将人的身高降序排列
优先满足身高高的人的位置
'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for person in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(person[1], person)
        return res
    
s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))