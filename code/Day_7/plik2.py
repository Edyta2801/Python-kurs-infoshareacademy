# otwieramy plik

plik = open('moj_plik.txt', 'r')

# odczytujemy pierwsza linijke
linijka = plik.readline()
print(len(linijka))

# sprawdzamy pozycje kursora w pliku
print(plik.tell())

# czytamy kolejna linijke
print(plik.readline())

# i kolejna
x = plik.readline()
print(x)

plik.close()