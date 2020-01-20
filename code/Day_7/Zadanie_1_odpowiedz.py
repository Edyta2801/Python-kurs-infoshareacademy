"""
Wymagania:
Utwórz 5 plików tekstowych z ulubionymi wierszami.
Następnie do każdego z tych plików dopisz na końcu pustą linię
oraz dodatkową linię "ulubiony wiersz <swopje_imię> nr <numer>"
"""
wiersz_1 = "wiersz_1"
wiersz_2 = "wiersz_2"
wiersz_3 = "wiersz_3"
wiersz_4 = "wiersz_4"
wiersz_5 = "wiersz_5"

wiersze = [wiersz_1, wiersz_2, wiersz_3, wiersz_4, wiersz_5]


# wersja 1
for i, wiersz in enumerate(wiersze):
    with open(f"wiersz_{i+1}.txt", 'w') as plik:
        plik.write(wiersz)

moje_imie = "Tomasz"
for i, wiersz in enumerate(wiersze):
    with open(f"wiersz_{i+1}.txt", 'a') as plik:
        plik.write(f"\n{moje_imie} nr {i+1}")

# wersja 2
# for i, wiersz in enumerate(wiersze):
#     with open(f"wiersz_{i+1}.txt", 'a+') as plik:
#         plik.write(wiersz+f"\n{moje_imie} nr {i+1}\n")
