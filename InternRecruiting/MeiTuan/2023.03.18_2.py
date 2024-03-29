'''
算法岗2023-03-18 2.彩带

时间限制：3000 MS
内存限制：589824 KB
题目描述：
小美现在有一串彩带，假定每一厘米的彩带上都是一种色彩。
因为任务的需要，小美希望从彩带上截取一段，使得彩带中的颜色数量不超过K种。
显然，这样的截取方法可能非常多。于是小美决定尽可能长地截取一段。
你的任务是帮助小美截取尽量长的一段，使得这段彩带上不同的色彩数量不超过K种。
输入描述：
第一行两个整数N,K，表示彩带有N厘米长，你截取的一段连续的彩带不能超过K种颜色。
接下来1行N个整数，每个整数表示一种色彩，相同的整数表示相同的色彩。
1<=N,K<=5000，彩带上的颜色数字介于[1,2000]之间。
输出描述：
一行，一个整数，表示选取的彩带的最大长度。
样例输入：
6 3
1 2 3 2 1 4 5 1
样例输出：
5
'''
# 100%
def max_length(colors, K):
    left = right = 0
    max_len = 0
    window = dict()
    while right < len(colors):
        if colors[right] in window:
            window[colors[right]] += 1
        else:
            window[colors[right]] = 1
        while len(window) > K:
            window[colors[left]] -= 1
            if window[colors[left]] == 0:
                del window[colors[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1
    max_len = max(max_len, right - left)
    return max_len


if __name__ == "__main__":
    colors = [1, 2, 3, 2, 1, 4, 5, 1]
    K = 3
    res = max_length(colors, K)
    print(res)