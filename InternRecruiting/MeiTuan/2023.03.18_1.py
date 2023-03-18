'''
算法岗2023-03-18 1.捕获

时间限制：3000 MS
内存限制：589824 KB
题目描述：
小美在玩一项游戏。该游戏的目标是尽可能抓获敌人。
敌人的位置将被一个二维坐标(x, y)所描述。
小美有一个全屏技能，该技能能一次性将若干敌人一次性捕获。
捕获的敌人之间的横坐标的最大差值不能大于A，纵坐标的最大差值不能大于B。
现在给出所有敌人的坐标，你的任务是计算小美一次性最多能使用技能捕获多少敌人。
输入描述：
第一行三个整数N,A,B，表示共有N个敌人，小美的全屏技能的参数A和参数B。
接下来N行，每行两个数字x,y，描述一个敌人所在的坐标。
1<=N<=500，1<=A,B<=100，1<=x,y<=1000。
输出描述：
一行，一个整数表示小美实用技能单次所可以捕获的最多数量。
样例输入：
3 1 1
1 1
1 2
1 3
样例输出：
2
'''

# 27%
def max_enemies(enemies, A, B):
    enemies.sort()
    left = right = 0
    max_count = 0
    window = []
    while right < len(enemies):

        while window and (enemies[right][0] - window[0][0] > A or enemies[right][1] - window[0][1] > B):
            window.pop(0)
        window.append(enemies[right])
        right += 1

        max_count = max(max_count, len(window))
    return max_count


if __name__ == "__main__":
    enemies = [[1, 1], [1, 2], [1, 3]]
    A, B = 1, 1
    res = max_enemies(enemies, A, B)
    print(res)
