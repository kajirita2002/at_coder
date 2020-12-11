# ans = 0
# n = input()
# for bit in range(1 << n):
#     #初期化
#     for i in range(n):
#         if bit & (1 << i):
#             #処理１
#             print()
#         else:
#             #処理2
#             print()
#     #処理
# print("処理")




#------------------------

s = input()
n = len(s)

ans = 0

for bit in range(1 << (n - 1)):
    # 各場合で式 f を生成する
    f = s[0]

    for i in range(n - 1):
        if bit & (1 << i):
            # フラグが立っているならば "+" を式の末尾に追加する
            f += "+"
        f += s[i + 1]

    ans += sum(list(map(int, f.split("+"))))

print(ans)
