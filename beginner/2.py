# 四則演算
# 倍数判定
a, b = map(int, input().split())
if a * b % 2:
    print('Odd')
else:
    print('Even')
