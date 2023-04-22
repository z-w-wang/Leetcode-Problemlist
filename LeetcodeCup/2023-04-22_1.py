from typing import List
class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        ops_num =  len(supplies) - len(supplies) // 2
        for _ in range(ops_num):
            minnum = 2001
            idx = -1
            for i in range(len(supplies) - 1):
                if supplies[i] + supplies[i + 1] < minnum:
                    minnum = supplies[i] + supplies[i + 1]
                    idx = i
            supplies = supplies[:idx] + [minnum] + supplies[idx+2:]
        return supplies