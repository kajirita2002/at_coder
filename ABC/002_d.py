import itertools

def dfs(i, group):
    global ans
    # 再帰のもの
    if i == n:
        # group内の全員が知り合い同士か
        flag = True
        # group 内から2人選ぶ組み合わせのループ
        # [(a, b), (a, c), (b, c)]など
        for i in itertools.combinations(group, 2):
            # 1人でも知り合いじゃなければ終了
            if friend[i[0]][i[1]] == 0:
                flag = False
                break
        # flagたったらansにgroup
        if flag:
            ans = max(ans, len(group))
    else:
        dfs(i + 1, group)
        dfs(i + 1, group + [i])


n, m = map(int, input().split())
# friendはfriend[[0],[0],[0],[0],[0]]から始まる
friend = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    # マップの数に変換する
    friend[x-1][y-1] = 1
    friend[x-1][y-1] = 1

ans = 0
dfs(0, [])
print(ans)