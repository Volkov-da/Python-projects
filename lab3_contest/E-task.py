import math

x = int(input())
c = 2
while c < x:
    c *= 2
print(int(math.log2(c)))
