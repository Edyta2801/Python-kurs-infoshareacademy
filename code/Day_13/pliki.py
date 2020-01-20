import shutil, os, send2trash

# użycie dysku
print(shutil.disk_usage('c:\\'))

# bieżący folder roboczy - na starcie będzie
# to folder, w którym uruchomiliśmy projekt/moduł
print(os.getcwd())

# zmieniamy folder roboczy
os.chdir('c:\\')
print(os.getcwd())

# tworzymy katalog
os.mkdir('c:\\pyta')

# kopiujemy drzewo - czyli wskazany folder oraz wszystkie
# podfoldery i pliki wewnątrz niego
shutil.copytree('c:\\day8', 'c:\\dzien8')

# przeniesienie folderu i wszystkich jego podfolderów
# i plików do innej lokalizacji
shutil.move('c:\\dzien8', 'c:\\dzien888')

# usunięcie pliku
# os.unlink('C:\\dzien888\\prep\\reszta.py')

# usunięcie folderu
#os.rmdir('c:\\aaaaa')

# usuniecie folderu wraz z całą zawartością wewnątrz
# shutil.rmtree('c:\\dzien888')

# os.listdir() - zwraca listę z zawartością folderu
for file in os.listdir('c:\\dzien888'):
    print(file)

# wysyłamy plik do kosza
# send2trash.send2trash('C:\\dzien888\\prep\\reszta.py')

# os.walk() zwraca tuple z 3 elementami:
# bieżący folder,
# listę podfolderów w bieżącym folderze,
# listę plików w bieżącym folderze
for folder_aktualny, podfoldery, pliki in os.walk('C:\\dzien888'):
    print('Obecny folder to:', folder_aktualny)

    for podkatalog in podfoldery:
        print('SUBFOLDER wew. folderu {} : {}'.format(folder_aktualny, podkatalog))

    for plik in pliki:
        print('Plik wew. folderu {} : {}'.format(folder_aktualny, plik))

    print()


my_dir = os.getcwd()
# os.path.abspath() zwraca całkowitą ścieżkę dla pliku/folderu
dir = os.path.abspath(my_dir)
print(dir)

# właściwości dla elementu
print(os.stat('C:\\dzien888\\Foto\\wakacje_7.jpg'))



