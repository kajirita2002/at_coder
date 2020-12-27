# pythonだとデフォルトの再帰処理回数の上限に引っかかってしまうので、それを変更
import sys
sys.setrecursionlimit(1000000)


# x, y = 始点
def dfs(x, y):
    d[x][y] = 1
    # 移動4方向をループ
    for i in range(4):
        # nxとnyは移動した時のx座標とy座標
        nx = x + dx[i]
        ny = y + dy[i]

        # nx と ny が
        # 街の範囲内か(0 <= nx and nx < n and 0 <= ny and ny < m)
        # 行ったことがないか(d[nx][ny] == 0)
        # 塀ではないか(c[nx][ny] != "#")
        # を判定
        if 0 <= nx and nx < n and 0 <= ny and ny < m and d[nx][ny] == 0 and c[nx][ny] != "#":
                # 人を進めて再帰
                dfs(nx, ny)

# n = hight, m = width
n, m = map(int, input().split())
# c = 横が一緒、縦が別の配列
c = [list(input()) for _ in range(n)]

# 到達したかどうか（0は未到達、1は到達済み）
d = [[0] * m for _ in range(n)]

# 移動する4方向　[上, 右, 左, 下]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# スタート地点から dfs を始める
for i in range(n):
    for j in range(m):
        if c[i][j] == "s":
            dfs(i, j)

# ゴール地点に到達したかどうか
for i in range(n):
    for j in range(m):
        # d[i][j]が到達すれば１でtrue, 到達しなければ0でfalse
        if c[i][j] == "g" and d[i][j]:
            print("Yes")
            exit()
print("No")