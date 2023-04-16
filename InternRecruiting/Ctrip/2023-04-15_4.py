'''
2023-04-15 算法岗 4

题目描述：
游游拿到了一个01串，该字符串仅由'0'和'1'两种字符组成，且第一个字符保证是1。
由于该字符串过长，游游用一个大小为n的数组表示该字符串。
第一个元素a1表示字符串开头有a1个'1'字符，第二个元素a2表示紧接着有a2个'0'字符，第三个元素a3表示紧接着有a3个'1'字符...
以此类推，这样就表示了一个长度为sum(ai)的01串。
游游想知道，该01串共有多少个非空回文子串（连续子串）？由于答案过大，请对10^9+7取模。

输入描述
第一行一个正整数n，表示数组的大小。
第二行输入n个正整数ai，代表数组的元素。
1<=n<=1000
1<=ai<=10^9

输出描述
回文子串的数量，答案对10^9+7取模。

输入示例
1
3

输出示例
6
'''
# 思路
'''
先计算相同字符内部的回文串数量(ai + 1) * ai // 2
再计算不同字符组成的回文串数量
以其中一个块为中心，向两边拓展，直到遇到两个数量不一致的块，取其最小值。
时间复杂度O(n^2)
'''
n = int(input())
line1 = input().strip().split(' ')
nums = list(map(int, line1))
res = 0
mod = 10 ** 9 + 7
for num in nums:
    res += (num + 1) * num // 2
    res %= mod
for i in range(len(nums)):
    p = 1
    while i - p >= 0 and i + p < len(nums):
        if nums[i + p] == nums[i - p]:
            res += nums[i + p]
            res %= mod
        else:
            res += min(nums[i + p], nums[i - p])
            res %= mod
            break
        p += 1
print(res)