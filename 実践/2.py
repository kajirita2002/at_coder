# H, W, Nがそれぞれ縦の枚数、横の枚数、プレイヤーの人数
H, W, N = [int(x) for x in input().split()]

# 初期配置の入力を受け取る
init_cards = [input().split() for _ in range(H)]

# めくった回数
L = int(input())

# 各プレイヤーのトランプの枚数のリストを定義
results = [0] * N

# プレイヤーを指定する変数を定義
who = 0

# めくった回数だけ繰り返す
for i in range(L):
    # めくったトランプの縦横の位置をint型に変換し、1引いた後、変数に代入
    a, b, A, B = [int(x)-1 for x in input().split()]

    # 2枚のカードが揃った場合
    if init_cards[a][b] == init_cards[A][B]:
        # プレイヤーのトランプの枚数を2増やす
        results[who] += 2
    else:
        # 次のプレイヤーの番に移る
        who = (who + 1) % N

# プレイヤーごとに繰り返す
for res in results:
    # 取った枚数を出力
    print(res)