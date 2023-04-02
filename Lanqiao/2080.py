'''
2080.求和
标签: 2022, 省赛

直接暴力求解的时间复杂度为O(n^2)，对于2*10^5的数据规模不可取
前缀和
原式可化成：S = a1(a2 + a3 + ... + an) + a2(a3 + a4 + ... + an) + ... + an-1 * an
             = ∑(ai * suffix[i])
suffix[i] = sum(ai+1 + ai+2 + ... + an)
时间复杂度O(n)
'''
n = int(input())
line = input().strip().split(' ')
nums = list(map(int, line))

suffixs = [0] * n
for i in range(n - 2, -1, -1):
    suffixs[i] = suffixs[i + 1] + nums[i + 1]

res = 0
for i in range(n - 1):
    res += nums[i] * suffixs[i]
print(res)