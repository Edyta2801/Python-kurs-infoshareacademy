# lista imion
imiona = ['ala', 'ola', 'jola']

# plik nie istnieje wiec chcemy go stworzyc
# uzywamy tryb w lub a
# przy trybie r+ nie utworzy
with open('imiona3.txt', 'w') as plik:
    plik.writelines(imiona)

