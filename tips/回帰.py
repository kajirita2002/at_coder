def dfs(i, f):
    #　もしiがn-1と同じだったら
    if i == n - 1:
        # 式fをプラスがついているところで分けてそのリストの合計を返す。
        return sum(list(map(int, f.split("+"))))

    # 式 f の末尾に "+" を追加するかしないかして次の数字を追加
    return dfs(i + 1, f + s[i + 1]) + dfs(i + 1, f + "+" + s[i + 1])

# sum(list(map(int, f.split("+")))) => 式（文字列）+の部分で分けて実際に演算する
s = input()
n = len(s)

print(dfs(0, s[0]))