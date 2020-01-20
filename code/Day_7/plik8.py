
# ustawianie kursora
with open('moj_plik.txt', 'r') as plik:
    text = plik.read()
    print(len(text))

    # tu sprawdzamy jaki ostatni znak w pliku jest
    # jesli nie bedzie to spacja - kod 10 to jesli chcemy
    # dopisac kolejna linijke musimy do stringa dodac \n
    print(ord(text[-1]))



