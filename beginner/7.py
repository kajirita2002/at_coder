# sorted() 関数は括弧の中身を昇順にソートして、新しいリストを返します。reverse=True を付けることで降順にソートできます。役割が似た関数として sort() 関数がありますが、これは元のリストを入れ替えてしまうため注意が必要です。
# sortする (22, 12 11)
# a[::2]で偶数のインデックスを持っている数(2こおき,0から)、[1::2]で奇数のインデックスを回収(1から二個おき)
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
print(sum(a[::2]) - sum(a[1::2]))