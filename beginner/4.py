# for 文を用いた全探索
# シミュレーション
n = input()
a = list(map(int, input().split()))
 #　無限の創造
ans = float('inf')
for i in a:
    ans = min(ans, len(bin(i)) - bin(i).rfind('1') - 1)
print(ans)

n = input()
a = list(map(int, input().split()))
ans = float('inf')
for i in a:
    ans = min(ans, len(bin(i)) - bin(i).rfind('1') - 1)
print(ans)