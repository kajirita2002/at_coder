from collections import deque


def bfs():
    d = [[float("inf")] * w for i in range(h)]
    # direction
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # queを作成
    que = deque([])
    # queにスタート
    que.append((sx, sy))
    # 最初の位置なので0を代入
    d[sx][sy] = 0

    while que:
        # 先入れ先出し
        p = que.popleft()
        # もしゴールに着いたらbreak
        if p[0] == gx and p[1] == gy:
            break
        # 四方向に行く
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            # 範囲内で、黒でなくそこが黒塗りされていなければ
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
                # 移動したqueに追加
                que.append((nx, ny))
                # そこにいくまでの最短経路でかかるコストを更新
                d[nx][ny] = d[p[0]][p[1]] + 1
    # goalまでに最短経路でかかるコストをreturn
    return d[gx][gy]


h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]
sx, sy = 0, 0
gx, gy = h - 1, w - 1

# 白いマスを数える
white = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == ".":
            white += 1

res = bfs()
if 0 < res < float("inf"):
    # 白いマスの数から最短経路でかかるコスト分を引く
    # ゴールを黒いマスに変えることはできないためその分も引く
    print(white - res - 1)
else:
    print(-1)