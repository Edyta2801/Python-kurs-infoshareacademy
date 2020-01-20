
wynik = 3
lista_a = ["zero", "jeden", wynik]
wynik = 43
# lista_b = lista_a
# lista_b = lista_a[:]
lista_b = lista_a.copy()
lista_a.append("new element")

print("lista a:", lista_a)
print("lista b:", lista_b)
