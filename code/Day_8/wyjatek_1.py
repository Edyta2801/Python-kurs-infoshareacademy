# chcemy zapisac informacje do pliku

naglowek = ''
try:
    with open('dane.csv', 'r') as plik:
        naglowek = plik.readline()
except FileNotFoundError:
    print('Plik nie istnieje')

print(naglowek)


# ValueError
# SyntaxError
# ZeroDivisionError
# NameError
# TypeError
