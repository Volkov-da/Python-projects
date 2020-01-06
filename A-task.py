print('Введите число:')
x = int(input())
a = x // 100
b = x // 10 - a * 10
c = x - a * 100 - b * 10
summa = a + b + c
print('Ввод:', x)
print('Вывод:', summa)



