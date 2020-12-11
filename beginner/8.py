n = int(input())
d = sorted(list(map(int, [input() for i in range(n)])),reverse=True)
ans = 0
before_num = float('inf')
for i in d:
    if i < before_num:
        ans += 1
    before_num = i
print(ans)

n = int(input())
print(len(set(map(int, [input() for i in range(n)]))))