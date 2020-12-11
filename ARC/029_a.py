# n = int(input())
# t = [int(input()) for i in range(n)]

# ans = float("inf")


# for bit in range(1 << n):
#     a = 0
#     b = 0
#     for i in range(n):
#         if bit & (1 << i):
#             a += t[i]
#         else:
#             b += t[i]
#     ans = min(ans, max(a, b))
# print(ans)


# ----------------


def dfs(i, a, b):
    global ans
    if i == n:
        ans = min(ans, max(a, b))
    else:
        dfs(i + 1, a + t[i], b)
        dfs(i + 1, a, b + t[i])

n = int(input())
t = [int(input()) for i in range(n)]

ans = float("inf")

dfs(0, 0, 0)
print(ans)
