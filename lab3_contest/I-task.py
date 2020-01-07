m = 0
c = 1
while c != 0:
    c = int(input())
    if c > m:
        m = c
        i = 1
    elif c == m:
        i += 1

else:
    print(i)
