import os
import shutil

# folder z plikami do zmiany nazwy
folder = 'c:\\dzien888\\Foto'

# nazwa wspólna dla plików
root = 'wakacje'

# generujemy indeksy dla plików w folderze
for indeks, plik in enumerate(os.listdir(folder)):
    # print('fotka {} : indeks {}'.format(plik, indeks))

    # tworzymy ścieżkę starego pliku
    stary_plik = os.path.join(folder, plik)
    # print(stary_plik)

    # oddzielamy nazwę pliku od rozszerzenia
    # splitext - zwraca tupla, więc możemy od razu
    # rozpakować (przypisać) go do dwóch zmiennych
    nazwa_pliku, ext = os.path.splitext(plik)

    # tworzymy nową nazwę
    nowa_nazwa = root + '_' + str(indeks) + ext

    # tworzymy ścieżkę nowego pliku
    nowy_plik = os.path.join(folder, nowa_nazwa)
    # print(nowy_plik)

    # zmieniamy nazwe plikom
    shutil.move(stary_plik, nowy_plik)