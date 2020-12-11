r, g, b = map(int, input().split())
if (r * 100 + g * 10 + b * 1) % 4:
    print("NO")
else:
    print("YES")

# 別解
r, g, b = list(map(str, input().split()))
n = int(r+g+b)
if n % 4:
    print("NO")
else:
    print("YES")