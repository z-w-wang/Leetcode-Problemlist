from typing import List
'''
2395. 和相等的子数组
https://leetcode.cn/problems/find-subarrays-with-equal-sum/

哈希表，遍历就完了。
'''
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s = set()
        for i in range(len(nums) - 1):
            if (sum1 := nums[i + 1] + nums[i]) in s:
                return True
            else:
                s.add(sum1)
        return False

s = Solution()
print(s.findSubarrays([4,2,4]))