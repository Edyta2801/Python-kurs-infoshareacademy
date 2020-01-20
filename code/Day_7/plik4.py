
plik = open('moj_plik.txt')

# readlines() wczytuje linijki jako elementy listy
linijki = plik.readlines()

print(linijki)

print(linijki[0])

plik.close()
