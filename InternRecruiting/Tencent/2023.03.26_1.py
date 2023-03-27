'''
2023-03-26 算法岗 1
时间限制：C/C++ 1秒，其他语言2秒。
空间限制：C/C++ 262144K，其他语言 524288K。
题目描述：
在一场考试中有n道多选题，每道题目的答案都是A、B、C、D中的若干个（可能只有一个，也可能全选。）
现在牛牛知道自己做出的答案和牛妹做出的答案。
已知每道题全部选对得3分，部分选对得1分，选错不得分。
牛牛现在知道牛妹得了满分，他想知道自己的最终分数是多少？
输入描述：
第一行一个正整数n，代表选择题的总数。
第二行n个长度为1到4的、只包含ABCD的字符串，其中第i个字符串代表牛牛第i题做出的选择。
第三行n个长度为1到4的、只包含ABCD的字符串，其中第i个字符串表示牛妹第i题做出的选择。
1<=n<=10000
输出描述：
一个整数，代表牛牛的得分。
'''
# 100%
n = int(input().strip())
nn = input().strip().split(' ')
nm = input().strip().split(' ')

score = 0
for i in range(n):
    s = set(list(nm[i]))
    wrong = False
    for c in nn[i]:
        if c not in s:
            wrong = True
            break
        else:
            s.discard(c)
    if wrong:
        continue
    if len(s) > 0:
        score += 1
    else:
        score += 3
print(score)