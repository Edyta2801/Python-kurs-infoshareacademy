a = 3
b = 4

x = b / (2.0 + a)
print(x)

# najpierw wykona sie to co z prawej strony znaku =
# a dopiero potem nastapi przypisanie do zmiennej z lewej strony znaku =
w = 0.1 + 0.1 + 0.1 == 0.3

# hmmm przeciez powinno być True
print(w)

# zwiekszamy precyzje i widzimy, ze ludzkie 0.3 nie ma odpowiednika
# w komputerowym 0.3. Niektore warotsci komputer moze tylko podac
# w przyblizeniu
print("{:.17f}".format(0.3))

z = round(0.1 + 0.1 + 0.1, 10) == round(0.3, 10)
print(z)


