def dfs(x, y):
    # 陸を海にする
    field[x][y] = "x"

    # 移動4方向をループ
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # nx と ny が
        # 地図の範囲内か(0 <= nx and nx < 10 and 0 <= ny and ny < 10)
        # field[nx][ny]が島か判定(field[nx][ny] == "o")
        if 0 <= nx and nx < 10 and 0 <= ny and ny < 10 and field[nx][ny] == "o":
            # 移動する(oを深さ優先探索)
            dfs(nx, ny)

# 島のリストを取得
a = [list(input()) for _ in range(10)]

# 移動する4方向
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 埋め立てる海の1マスを全探索
for p in range(10):
    for q in range(10):
        # 海を見つけたら
        if a[p][q] == "x":
            # a を field にコピーしてそのマスを埋め立てる k[:]で aを完コピしたものを代入(初期化)
            field = [k[:] for k in a]
            # 埋める
            field[p][q] = "o"
            # 島の数
            count = 0
            # 埋め立てた上で dfs で島の数をカウント
            for i in range(10):
                for j in range(10):
                    # 陸があれば
                    if field[i][j] == "o":
                        # 陸を塗りつぶしていく
                        dfs(i, j)
                        count += 1
            # count (島の数)が1かどうか
            if count == 1:
                print("YES")
                exit()
print("NO")

# #方針
# 1. 再帰関数を用いて深さ優先探索をしていく。
# 2. 埋め立てする海を全検索して埋める→島の数をカウントする
# 3. 島を塗りつぶす(海にする)dfs関数を作る(現在地から4方に動く)