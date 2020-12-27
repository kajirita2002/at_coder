# 閉路の有無を調べる
def dfs(now, prev):
    global flag
    # 今いる頂点(g[now])から行ける頂点を順に next に入れてループ
    for next in g[now]:
        # 頂点が違うものであれば
        if next != prev:
            # 過去に訪れていれば
            if memo[next]:
                # 過去に訪れていれば閉路
                flag = False
            else:
                # 訪れた事を記録
                memo[next] = True
                # 次に移動
                dfs(next, now)


n, m = map(int, input().split())
# 点について空の配列を作る
g = [[] * n for i in range(n)]
# 辺=mをそれぞれu, vに代入
for i in range(m):
    u, v = map(int, input().split())
    # indexに直す
    u -= 1
    v -= 1
    # 配列に辺の反対側を代入
    g[u].append(v)
    g[v].append(u)

# 訪れたことがあるか
memo = [False for i in range(n)]

ans = 0
# 頂点をループ
for i in range(n):
    # 記録がなければ
    if not memo[i]:
        #
        flag = True

        dfs(i, -1)
        if flag:
            # 閉路がなければ木である
            ans += 1
print(ans)