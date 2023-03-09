'''
2379. 得到 K 个黑块的最少涂色次数

滑动窗口题
统计大小为k的窗口中有多少'w'，取最小值。
'''
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        res = count
        for i in range(len(blocks) - k):
            if blocks[i + k] == 'W':
                count += 1
            if blocks[i] == 'W':
                count -= 1
            res = min(res, count)
        return res
s = Solution()
print(s.minimumRecolors("WBBWWBBWBW", 7))