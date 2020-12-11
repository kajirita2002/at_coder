#(x + y) > t では t 秒後までに最短でも x + y 回は移動する必要があるため x + y の方が大きい場合は旅行プランが実行不可能。(x + y + t) % 2 では x + y + t の合計が 2 で割り切れない場合、つまり x + y と t の偶奇が異なる場合は「その場にとどまることは出来ない」という条件から通り過ぎてしまう。

n = int(input())
for i in range(n):
    t,x,y = map(int,input().split())
    if (x + y) > t or (x + y + t) % 2:
        print("No")
        exit()
print("Yes")
