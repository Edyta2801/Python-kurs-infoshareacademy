
path0 = "c:\myDocuments\newDocument"

# znowu cos nie tak, dlaczego lamie mi linie?
# ach bo odczytuje kawalek \n jako znak nowej linii
print(path0)

# mozemy zapisac jako raw string
path = r"c:\myDocuments\newDocument"
print(path)

# albo uzyc escape char - czyli podwojnego backslasha \\
path2 = "c:\myDocuments\\newDocument"
print(path2)

# ten Python to naprawde potrafi czary
print(path0[:4] + 'kot' * 3)