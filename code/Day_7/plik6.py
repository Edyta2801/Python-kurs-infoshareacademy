# uwazamy przy zapisywaniu plików!
# rozne tryby pracy z plikami

# with open('moj_plik.txt', 'a') as plik:
#     plik.write('Moja kolejna linijka z Pythona')

# with open('moj_plik.txt', 'r+') as plik:
    # jeśli zaczniemy zapisywaie od razu w trybie r+ lub w
    # to tekst zacznie byc wpisywany od poczatku pliku!
#     plik.write('xxxxxxxxxxxxxxa\n')

# przy zapisywaniu w trybie r+ lub w sami musimy
# ustawic kursor na końcu lini
with open('moj_plik.txt', 'r+') as plik:
    # idziemy na koniec pliku poleceniem read()
    plik.read()
    plik.write('Moja kolejna linijka dodana na końcu\n')
