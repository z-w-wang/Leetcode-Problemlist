'''
1616. 分割两个字符串得到回文串
https://leetcode.cn/problems/split-two-strings-to-make-palindrome/

模拟就行
'''
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        split_index = -1
        n = len(a)
        rev = 0
        for i in range(n // 2):
            if a[i] != b[n - 1 - i]:
                split_index = i
                break
        if split_index == -1:
            return True
        for i in range(split_index, n // 2):
            if b[i] != b[n - 1 - i]:
                rev = 1
                break
        for i in range(split_index, n // 2):
            if a[i] != a[n - 1 - i]:
                rev += 1
                break
        if rev == 2:
            rev = 0
            split_index = -1
            for i in range(n // 2):
                if b[i] != a[n - 1 - i]:
                    split_index = i
                    break
            if split_index == -1:
                return True
            for i in range(split_index, n // 2):
                if b[i] != b[n - 1 - i]:
                    rev = 1
                    break
            for i in range(split_index, n // 2):
                if a[i] != a[n - 1 - i]:
                    rev += 1
                    break
            if rev == 2:
                return False
        return True

s = Solution()
print(s.checkPalindromeFormation("pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmcvp"))