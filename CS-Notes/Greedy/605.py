from typing import List
'''
605. 种花问题
https://leetcode.cn/problems/can-place-flowers/

贪心就完事儿了
从一开始能种的都种上
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 or flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False
        
        res = 0
        if flowerbed[0] == flowerbed[1] and flowerbed[0] == 0:
            res += 1 
            flowerbed[0] = 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                res += 1
                if res >= n:
                    return True
                flowerbed[i] = 1
        if flowerbed[-1] == flowerbed[-2] and flowerbed[-1] == 0:
            res += 1 
        return res >= n
    
s = Solution()
print(s.canPlaceFlowers([0,0,1,0,0], 1))