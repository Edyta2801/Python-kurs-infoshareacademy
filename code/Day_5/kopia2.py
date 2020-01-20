# zakupy

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "plyn do naczyn"]

zakupy_styczen = [nabial, chemia]
print(zakupy_styczen)

zakupy_luty = zakupy_styczen.copy()
print(zakupy_luty)

zakupy_styczen[1].append("gabka do naczyn")

print(hex(id(zakupy_styczen[1])))
print(hex(id(zakupy_luty[1])))