# list comprehension
# str to list
imie = "walenty"
lista_imie = list(imie)
print(lista_imie)

# syntactic sugar
sweet_list = [element for element in lista_imie]
print(sweet_list)

kwadraty = [x**2 for x in range(101)]
print(kwadraty)


kwadraty_liczb_podzielnych_przez_2 = [x**2 for x in range(101) if x**2 % 2 == 0]
print(kwadraty_liczb_podzielnych_przez_2)




