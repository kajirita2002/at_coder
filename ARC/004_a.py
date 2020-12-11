



# --------------------------------------------------------------------




# math.sqrt(pow(x[k]-x[j], 2)+ pow(y[k]-y[j], 2))　これは三角形の辺の長さを出すもの
# list(range(n))はx[i]の初期化に必要
# for 文を二回回して全てのケースを探索する(全検索)
import math
n = int(input())
x = list(range(n))
y = list(range(n))
for i in range(n):
    x[i], y[i] = map(int, input().split())
ans = 0
print(x, y)

for j in range(n):
    for k in range(n):
        if math.sqrt(pow(x[k]-x[j],2) + pow(y[k]-y[j], 2)) > ans:
            ans = math.sqrt(pow(x[k]-x[j],2) + pow(y[k]-y[j], 2))
print(ans)