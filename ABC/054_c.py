import itertools

n, m = map(int, input().split())

path = [[False] * n for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    # index化
    a -= 1
    b -= 1
    # true
    path[a][b] = True
    path[b][a] = True

ans = 0

# 頂点を並び替える順列を生成してループ
for i in itertools.permutations(range(n), n):
    # 頂点1が始点
    if i[0] == 0:
        # 生成した順列の中をさらにループ
        for j in range(n):
            # n - 1 まで続いたら条件を満たすパスが存在する
            if j == n - 1:
                ans += 1
                break
            # i[j] から i[j + 1] に行くパスがなければ終了
            if not path[i[j]][i[j + 1]]:
                break

print(ans)