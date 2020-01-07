base = 10
a = 0
x = int(input())
while x > 0:
    digit = x % base
    x //= base
    a += digit
print(a)
