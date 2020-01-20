moj_plik = 'dlugosc_pliku.txt'

# with open('moj_plik.txt', 'r+') as plik:
    # dlugosci plikow nie mozna sprawdzic len()
    # plik.seek(len(plik))

import os

size = os.path.getsize(moj_plik)
print("Rozmiar pliku '{}' wynosi: {} bajtów".format(moj_plik, size))

with open('dlugosc_pliku.txt') as plik:
    tekst = plik.read()
    print(tekst)
    print("Dlugosc tekstu wynosi {} znaków".format(len(tekst)))

# skąd róznica?
# w utf-8 znak potrzebuje od 1 do 4 bajtów,
# no i jeszcze musi byc zapisana informacja o kodowaniu :)
