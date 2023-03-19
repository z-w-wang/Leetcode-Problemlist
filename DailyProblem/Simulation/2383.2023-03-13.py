from typing import List
'''
2383. 赢得比赛需要的最少训练时长
https://leetcode.cn/problems/minimum-hours-of-training-to-win-a-competition/

模拟就完事儿了。
'''
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        traintime = 0 if initialEnergy > (allenergy:=sum(energy)) else allenergy - initialEnergy + 1
        for ex in experience:
            if initialExperience <= ex:
                traintime += ex - initialExperience + 1
                initialExperience = ex + 1
            initialExperience += ex
        return traintime

s = Solution()
print(s.minNumberOfHours(5, 3, [1,4,3,2], [2,6,3,1]))