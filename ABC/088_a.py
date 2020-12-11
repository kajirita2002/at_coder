# 先に割ることであまりが1円で払えるかを考えることができる。
n, a = map(int, [input() for i in range(2)])
if (n % 500) > a:
    print('NO')
else:
    print('Yes')