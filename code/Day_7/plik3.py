
plik = open('moj_plik.txt')

print("To jest pierwsza linijka:")

# jesli w pliku linijka konczy sie znakiem nowej lini \n
# to przy drukowaniu musimy pozbawic printa tego znaku
print(plik.readline(), end='')

# jesli podamy liczbe, to przeczytamy konkretna ilosc znakow
#tresc = plik.read(26)

# jesli nie podamy to zostanie przeczytana tresc od biezacego
# miejsca kursora do konca pliku
tresc = plik.read()
print("read() odczyta od drugiej linijki:")
print(tresc)

# tell mowi o pozycji w jakiej znajduje sie kursor
print(plik.tell())

plik.close()