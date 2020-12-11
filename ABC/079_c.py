# def dfs(i, f, sum):
#     if i == 3:
#         if sum == 7:
#             print(f + "=7")
#             exit()
#     else:
#         dfs(i + 1, f + "+" + s[i + 1], sum + int(s[i + 1]))
#         dfs(i + 1, f + "-" + s[i + 1], sum - int(s[i + 1]))

# s = input()

# dfs(0, s[0], int(s[0]))

# --------------------------------------------
s = input()
for bit in range(1 << 3):
    f = s[0]
    sum = int(s[0])
    for i in range(3):
        if bit & (1 << i):
            f += "+"
            sum += int(s[i + 1])
        else:
            f += "-"
            sum -= int(s[i + 1])
        f += s[i + 1]
    if sum == 7:
        print(f + "=7")
        exit()
