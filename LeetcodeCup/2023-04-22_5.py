from typing import List
# 超时 O(3^(m*n))
class Solution:
    def getSchemeCount(self, n: int, m: int, chessboard: List[str]) -> int:
        unknown_pos = []
        board = [[''] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j + 2 < m and (chessboard[i][j] == 'R' and chessboard[i][j + 2] == 'B' or chessboard[i][j] == 'B' and chessboard[i][j + 2] == 'R') \
                    and (chessboard[i][j + 1] == 'B' or chessboard[i][j + 1] == 'R'):
                    return 0
                if chessboard[i][j] == '?':
                    unknown_pos.append([i, j])
                board[i][j] = chessboard[i][j]

        for j in range(m):
            for i in range(n - 2):
                if (chessboard[i][j] == 'R' and chessboard[i + 2][j] == 'B' or chessboard[i][j] == 'B' and chessboard[i + 2][j] == 'R') \
                    and (chessboard[i + 1][j] == 'B' or chessboard[i + 1][j] == 'R'):
                    return 0
                
        def anti_state(state):
            if state == 'R':
                return 'B'
            if state == 'B':
                return 'R'
            
        def is_chess(x, y):
            return board[x][y] == 'B' or board[x][y] == 'R'
        
        def judge(x, y, state):
            if x - 2 >= 0 and board[x - 2][y] == anti_state(state) and is_chess(x - 1, y) or \
                x + 2 < n and board[x + 2][y] == anti_state(state) and is_chess(x + 1, y) or \
                y - 2 >= 0 and board[x][y - 2] == anti_state(state) and is_chess(x, y - 1) or \
                y + 2 < m and board[x][y + 2] == anti_state(state) and is_chess(x, y + 1):
                return 0
            return 1
        
        choose = {'B', 'R', '.'}
        def dfs(idx):
            if idx == len(unknown_pos):
                return 1
            res = 0
            ux, uy = unknown_pos[idx]

            for state in choose:
                if judge(ux, uy, state):
                    board[ux][uy] = state
                    # if state == '.':
                    #     res *= 2
                    #     break
                    res += dfs(idx + 1)
            board[ux][uy] = '?'
            return res
        return dfs(0)

s = Solution()
print(s.getSchemeCount(3, 3, ["?R?","B?B","?R?"]))