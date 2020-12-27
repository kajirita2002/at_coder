from collections import deque


def bfs():
    d = [[float("inf")] * c for i in range(r)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    que.append((sy, sx))
    d[sy][sx] = 0

    while que:
        p = que.popleft()
        if p[0] == gy and p[1] == gx:
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[gy][gx]


r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
# index化
sx -= 1
sy -= 1
gy -= 1
gx -= 1
maze = [list(input()) for i in range(r)]

print(bfs())