'''
算法岗2023-03-18 3.回文串

时间限制：3000 MS
内存限制：589824 KB
题目描述：
现在小美获得了一个字符串。小美想要使得这个字符串是回文串。
小美找到了你。你可以将字符串中至多两个位置改为任意小写英文字符“a”-“z”。
你的任务是帮助小美在当前制约下，获得字典序最小的回文字符串。
数据保证能在题目限制下形成回文字符串。
注:回文字符串:即一个字符串从前向后和从后向前是完全一致的字符串。
例如字符串abcba,aaaa,acca都是回文字符串。字符串abcd,acea都不是回文字符串。
输入描述：
一行，一个字符串。字符串中仅由小写英文字符构成。
保证字符串不会是空字符串。
字符串长度介于[1,100000] 之间。
输出描述：
一行，一个在题目条件限制下所可以获得的字典序最小的回文字符串。
样例输入：
acca
样例输出：
aaaa
'''
# 27%
def make_palindrome(s):
    n = len(s)
    mid = n // 2
    i = 0
    j = n - 1
    changes = 0

    s_list = list(s)

    while i < mid:
        if s_list[i] < s_list[j]:
            s_list[j] = s_list[i]
            changes += 1
        elif s_list[i] > s_list[j]:
            s_list[i] = s_list[j]
            changes += 1
        i += 1
        j -= 1

    if changes == 0:
        i = 0
        j = n - 1
        while i < mid:
            if s_list[i] != 'a':
                s_list[i] = 'a'
                s_list[j] = 'a'
                break
            i += 1
            j -= 1
        return ''.join(s_list)
    elif changes == 1:
        s_list[n // 2] = 'a'
        return ''.join(s_list)
    elif changes > 2:
        return ""
    return ''.join(s_list)

if __name__ == '__main__':
    print("abcda", " -> ", make_palindrome("abcda"))
    print("abcba", " -> ", make_palindrome("abcba"))
    print("abba", " -> ", make_palindrome("abba"))
    print("abcd", " -> ", make_palindrome("abcd"))