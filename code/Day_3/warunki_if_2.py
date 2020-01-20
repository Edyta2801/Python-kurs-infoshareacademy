name = input("Podaj Imie: ")

# jesli ostatnia litera jest 'a' to najprawdopodobniej kobieta
if name.endswith("a") and not name == "Jan Maria":
    print("Hej {}, jesteś najpewniej kobietą".format(name))

# jezeli napisze Jan Maria to witamy Pana Rokite
if name == "Jan Maria":
    print("Witaj, Panie Rokita.")

else:
    print("Hej {}, jesteś chyba mężczyzną".format(name))


