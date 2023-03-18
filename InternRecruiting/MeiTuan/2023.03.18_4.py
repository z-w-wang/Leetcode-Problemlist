'''
算法岗2023-03-18 3.回文串

时间限制：3000 MS
内存限制：589824 KB
题目描述：
现在商店里有N个物品，每个物品有原价和折扣价。
小美想要购买商品。小美拥有X元，共Y张折扣券。
小美需要最大化购买商品的数量，并在所购商品数量尽量多的前提下，尽量减少花费。
你的任务是帮助小美求出最优情况下的商品购买数量和花费的钱数。
输入描述：
第一行三个整数，以空格分开，分别表示N,X,Y。
接下来N行，每行两个整数，以空格分开，表示一个的原价和折扣价。
1<=N<=100，1<=X<=5000，1<=Y<=50，每个商品原价和折扣价均介于[1,50]之间。
输出描述：
一行，两个整数，以空格分开。第1个数字表示最多买几个商品，第2个数字表示在满足商品尽量多的前提下所花费的最少的钱数。
样例输入：
3 5 1
4 3
3 1
6 5
样例输出：
2 5
'''
# 0%
def max_items_and_min_cost(N, X, Y, items):
    items.sort()  # Sort items by original price in ascending order
    dp = [[[0] * (X+1) for _ in range(Y+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(Y+1):
            for k in range(X+1):
                dp[i][j][k] = dp[i-1][j][k]  # Not buying the current item
                if k >= items[i-1][0]:
                    # Buying the current item without a discount coupon
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-items[i-1][0]] + 1)
                if j >= 1 and k >= items[i-1][1]:
                    # Buying the current item with a discount coupon
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k-items[i-1][1]] + 1)

    count = 0
    cost = 0
    for j in range(Y+1):
        for k in range(X+1):
            if dp[N][j][k] > count:
                count = dp[N][j][k]
                cost = k

    return count, cost

# Sample input
N = 3
X = 5
Y = 1
items = [
    (4, 3),
    (3, 1),
    (6, 5)
]

# Sample output
print(max_items_and_min_cost(N, X, Y, items))  # Output: (2, 5)