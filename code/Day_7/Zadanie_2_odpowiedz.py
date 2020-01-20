"""
Wymagania:
Utwórz plik dane_osobowe.csv z 10 wierszami, zawierającymi dane:
Imię, Nazwisko, Data_Urodzenia, Płeć, Adres_Ulica, Adres_Nr_Domu, Adres_Nr_Lokalu, Adres_Kod_Pocztowy, Adres_Miasto

Następnie na podstawie utworzonego pliku utwórz dwa nowe:
dane_kobiety.csv
dane_mezczyzni.csv
zawierające odpowiednie rekordy z pliku dane_osobowe.csv
"""
def add_newline_to_each_string_in_list(string_list):
    return [line if line[-1]=='\n' else line+'\n' for line in string_list]


def append_to_file(file_name, lines):
    """
    Funkcja dodająca linijkę do pliku o podanej nazwie
    (string, list)
    :param file_name:
    :param lines:
    :return:
    """
    with open(file_name, 'a+') as f:
        lines = [line if line[-1]=='\n' else line+'\n' for line in lines ]
        f.writelines(lines)


with open('dane_osobowe.csv', 'w') as csvfile:
    rekord="Katarzyna,Kowalska,1982,K,Żarnowiecka,12,2,20-654,Lublin"
    rekord2="Janek,Kowalski,1982,M,Żarnowiecka,12,2,20-654,Lublin"
    rekord3="Janek,Kowalski,1982,M,Żarnowiecka,12,2,20-654,Lublin"
    rekord4="Janina,Kowalska,1982,K,Żarnowiecka,12,2,20-654,Lublin"
    rekord5="Janek,Kowalski,1982,M,Żarnowiecka,12,2,20-654,Lublin"

    rekordy =[rekord, rekord2, rekord3, rekord4, rekord5]
    rekordy = add_newline_to_each_string_in_list(rekordy)
    csvfile.writelines(rekordy)


with open('dane_osobowe.csv', 'r') as csvfile:
    linie = csvfile.readlines()
    print(linie)
    for l in linie:
        plec = l.split(',')[3]
        print(plec)
        if plec == "K":
            append_to_file('kobiety.csv', [l])
        elif plec == "M":
            append_to_file('mezczyzni.csv', [l])
        else:
            print("Podano nieprawidłowy kod płci.")
