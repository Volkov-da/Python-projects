x0 = int(input())
y0 = int(input())
x1 = int(input())
y1 = int(input())
if x0 == x1 or y0 == y1:
    print('YES')
else:
    if abs(x0 - x1) == abs(y0 - y1):
        print('YES')
    else:
        print('NO')
