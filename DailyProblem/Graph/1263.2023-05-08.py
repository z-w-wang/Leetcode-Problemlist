from typing import List
from collections import deque
MOVE = ((0, -1), (0, 1), (1, 0), (-1, 0))

'''
1263. 推箱子
https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/

0-1 DFS
用seen记录走过的格子状态和盒子的位置状态
广度遍历搜索每一步的状态
由于只需记录格子的移动次数 所以用双向队列deque模拟0-1BFS的过程
'''

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 'B':
                    box_pos_row, box_pos_col = i, j
                elif x == 'S':
                    person_pos_row, person_pos_col = i, j
        visited = dict()
        visited[(box_pos_row, box_pos_col, person_pos_row, person_pos_col)] = 0

        def check(r: int, c: int) -> bool:
            return r >= 0 and r < len(grid) and \
                c >= 0 and c < len(grid[0]) and \
                    grid[r][c] != '#'

        q = deque([(box_pos_row, box_pos_col, person_pos_row, person_pos_col)])

        while q:
            pre_state = q.popleft()
            if grid[pre_state[0]][pre_state[1]] == 'T':
                return visited[pre_state]

            for move_row, move_col in MOVE:
                cur_person_pos_row = pre_state[2] + move_row
                cur_person_pos_col = pre_state[3] + move_col
                if not check(cur_person_pos_row, cur_person_pos_col):
                    continue
                cur_box_pos_row, cur_box_pos_col = pre_state[0], pre_state[1]

                if cur_person_pos_row == cur_box_pos_row and \
                        cur_person_pos_col == cur_box_pos_col:
                    cur_box_pos_row += move_row
                    cur_box_pos_col += move_col
                    cur_state = (cur_box_pos_row, cur_box_pos_col,
                                 cur_person_pos_row, cur_person_pos_col)

                    if not check(cur_box_pos_row, cur_box_pos_col) or \
                            cur_state in visited and visited[cur_state] <= visited[pre_state] + 1:
                        continue

                    visited[cur_state] = visited[pre_state] + 1
                    q.append(cur_state)

                else:
                    cur_state = (cur_box_pos_row, cur_box_pos_col,
                                 cur_person_pos_row, cur_person_pos_col)

                    if cur_state in visited and visited[cur_state] <= visited[pre_state]:
                        continue

                    visited[cur_state] = visited[pre_state]
                    q.appendleft(cur_state)

        return -1

s = Solution()
grid = \
    [[".",".","#",".",".",".",".","#"],
     [".","B",".",".",".",".",".","#"],
     [".",".","S",".",".",".",".","."],
     [".","#",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","."],
     [".",".",".","T",".",".",".","."],
     [".",".",".",".",".",".",".","#"],
     [".","#",".",".",".",".",".","."]]

print(s.minPushBox(grid=grid))