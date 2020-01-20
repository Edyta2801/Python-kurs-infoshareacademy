# deklarowanie list
lista = []
lista1 = [2, 3, 4, 5, 6, 7, 8]
lista2 = ["kwiatek", "woda", "doniczka", "ziemia"]

# konstruktor
zakres = range(2,5)
print(zakres)
lista3 = list(zakres)
print(lista3)

# w listach moga byc rozne elementy
lista4 = ["zero", 1, 2.0, range(5)]
print(lista4)

# str to list
imie = "walenty"
lista_imie = list(imie)
print(lista_imie)

print(len(lista4))

# syntactic sugar
sweet_list = [element for element in lista_imie]
print(sweet_list)

# kwadraty = [x**2 for x in range(101)]
#print(kwadraty)

# listy mozna indeksowac
print(sweet_list[1])
print(lista3[2])

# mozna slicowac ciac
print(sweet_list[1:5])
print(sweet_list[1:6:2])

# funkcje wbudowane
sweet_list.append("nowy")
print(sweet_list)

sweet_list.extend(lista1)
print(sweet_list)

# lista do str
s = ["s", "a", "b", "4"]

wyraz = "".join(s)
print(wyraz)





