from typing import List
class Solution:
    def adventureCamp(self, expeditions: List[str]) -> int:
        max_appear_num = 0
        idx = -1
        seen = set()
        init = expeditions[0].split('->')
        for camp in init:
            seen.add(camp)
        for i in range(1, len(expeditions)):
            camps = expeditions[i].split('->')
            if expeditions[i] == '':
                continue
            count = 0
            for camp in camps:
                if camp not in seen:
                    count += 1
                    seen.add(camp)
            if count > max_appear_num:
                max_appear_num = count
                idx = i
        return idx