 # +1しないと20の場合19までしかない
 # list('13')で['1', '3']に分割し、イテレーターをlist形にキャストする

n, a, b = map(int, input().split())
ans = 0
for i in range(n+1):
    if a <= sum(map(int, list(str(i)))) <= b:
        ans += i
print(ans)
