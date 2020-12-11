def dfs(i, f):
    if i == n - 1:
        return sum(list(map(int, f.split("+"))))
    return dfs(i + 1, f + s[i + 1]) + dfs(i + 1, f + "+" + s[i + 1])

s = input()
n = len(s)
ans = 0
for bit in range(1 << (n - 1)):
    # 初期化
    f = s[0]
    for i in range(n - 1):
        if bit & (1 << i):
            # 2分の1で行う処理
            f += "+"
        # 次の文字列に移動
        f += s[i + 1]
    ans +=  sum(map(int, f.split("+")))
print(ans)