# おつりの金額
a = 1000 - int(input())

# variation
v = [1, 5, 10, 50, 100, 500]
ans = 0

# 上の方(500)から割っていく
for i in range(1, 7):
    t = a // v[-i]
    a -= t * v[-i]
    ans += t

print(ans)