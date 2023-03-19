from math import gcd
'''
1625. 执行操作后字典序最小的字符串
https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations/

可以直接模拟
轮转最多轮转n次，n为s的长度
累加最多加10次
所以模拟 时间复杂度为O(100*n^2)

由裴蜀定理xb - yn = z → z = gcd(b, n)
可以以gcd(b, n)为间隔轮转到n

每次变换让其字典序最小，只需让s_list[1]最小即可，时间复杂度减小到O(n * k^2), k < 10
'''
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s_list = list(map(int, list(s)))
        min_s = s
        n = len(s)
        g = gcd(n, b)
        for _ in range(0, n, g):
            s_list = s_list[g: ] + s_list[: g]

            for _ in range(10):
                for i in range(1, n, 2):
                    s_list[i] = (s_list[i] + a) % 10
                if b % 2:
                    for _ in range(10):
                        for i in range(0, n, 2):
                            s_list[i] = (s_list[i] + a) % 10

                        min_s = min(min_s, "".join(map(str, s_list)))
                else:
                    min_s = min(min_s, "".join(map(str, s_list)))
        return min_s
    
    # 100%做法，狠狠裴蜀
    def findLexSmallestString_100pct(self, s, a, b):
        n = len(s)
        nums = list(map(int, list(s)))
        ans = nums
        g = gcd(b, n)
        for _ in range(0, n, g):
            nums = nums[g: ] + nums[: g]
            m1 = gcd(10, a)
            
            n1 = nums[1]
            if (mo:=n1 % m1):
                minus = n1 - mo
            else:
                minus = n1

            for i in range(1, n, 2):
                nums[i] = (nums[i] - minus) % 10

            if b & 1:
                n0 = nums[0]
                if (mo:=n0 % m1):
                    minus = n0 - mo
                else:
                    minus = n0

                for i in range(0, n, 2):
                    nums[i] = (nums[i] - minus) % 10
                
            ans = min(ans, nums)

        return ''.join(map(str, ans))
s = Solution()
print(s.findLexSmallestString_100pct("43987654", 7, 3))