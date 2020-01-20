"""
Wymagania:
Wypisać liczby należących ciagu fibonacciego
do podanej liczby n

Podpowiedź:
Ciąg Fibonacciego:
0, 1, 1, 2, 3, 5, 8, 13 ...

Rekurencyjnie:
[x - 2] + [x - 1] = [x]

Liniowo:
temp
y = x - 2
x = x - 1
"""


n = int(input("Podaj liczbę:"))

x = 0
y = 1

print(x, end=' ')
print(y, end=' ')

while x + y < n:
    # mało pythonowo - zmienna tymczasowa
    # temp = x
    # x = y
    # y = x + temp
    # bardzo pythonowo
    x, y = y, x+y
    print(y, end=' ')

