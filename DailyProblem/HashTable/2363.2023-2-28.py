from typing import List

# 2363. 合并相似的物品
'''
哈希表记录，再排序
记录O(l1+l2), 排序O((l1+l2)log(l1+l2))
'''
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        sd = dict()
        for k, v in items1:
            if k in sd:
                sd[k] += v
            else:
                sd[k] = v
        for k, v in items2:
            if k in sd:
                sd[k] += v
            else:
                sd[k] = v
        return sorted([[k, v] for k, v in sd.items()])
    
s = Solution()
print(s.mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]))