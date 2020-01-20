wiek = input("Podaj wiek: ")

# wszystko co uzytkownik poda jest stringiem, nawet liczby
print(type(wiek))

# musimy zamienic str na int aby moc wykonac arytmetyke
rok_ur = 2018 - int(wiek)

print("Twoj rok urodzenia to {}".format(rok_ur))

wzrost = input("podaj wzrost: ")

# formatowanie wartosci liczbowych
print("Twoj wzrost w centymetrach to {:.2f}".format(float(wzrost)))

