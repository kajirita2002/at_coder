a, b, c = map(int, input().split())
idx = 0
for id, i in enumerate(range(101)):
    if a*i%b == c:
        idx = id
        print("YES", id)
        exit()
print("NO", idx)
