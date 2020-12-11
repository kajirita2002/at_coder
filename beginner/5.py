
# 今回の問題は入力形式が縦に 4 つ並んでいる形式のため for 文で繰り返す形を取っています。a = int(input()) というコードを 4 つ縦に書くのを省略した書き方です。

#　範囲に制限がある →　全部の組み合わせを試せる
# 全部の組み合わせ　→ for i j kを使う
# 何通りか →　適応したものが発見できたら+1追加していく。

a, b, c, x = map(int, [input() for i in range(4)])
ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500 * i + 100 * j + 50 * k == x:
                ans += 1
print(ans)