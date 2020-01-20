# noinspection SpellCheckingInspection
class Pracownik(object):
    """Klasa Pracownik"""

    liczba_pracownikow = 0
    roczna_podwyzka = 5

    def __init__(self, imie, nazwisko):
        """Konstruktor (str, str, str)"""
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__stanowisko = None
        Pracownik.liczba_pracownikow += 1

    def wypisz_imie(self):
        """Wypisuje imię pracownika"""
        print(str(self.__imie).capitalize())

    def nazwisko_get(self):
        return str(self.__nazwisko).upper()

    @property
    def stanowisko(self):
        """Zwraca stanowisko pracownika"""
        if self.__stanowisko is not None:
            return str(self.__stanowisko).capitalize()

    @stanowisko.setter
    def stanowisko(self, nazwa):
        """Ustawia stanowisko pracownika (str)"""
        if str(nazwa).isalpha():
            self.__stanowisko = nazwa

    @stanowisko.deleter
    def stanowisko(self):
        """Usuwa stanowisko pracownika"""
        print('Usuwam stanowisko')
        self.__stanowisko = None

    @classmethod
    def okresl_rocz_podw(cls, wartosc):
        """Zmienia wartość domyślnej podwyżki.
        Metoda klasy - zmienia pole klasy"""
        if wartosc > 8:
            cls.roczna_podwyzka = 8
        else:
            cls.roczna_podwyzka = wartosc

    @classmethod
    def z_pensja(cls, imie, stan, pensja):
        """Alternatywny konstruktor"""
        prac = cls(imie, stan)
        # przed zwróceniem instancji, musimy zaktualizować jej pola
        prac.wynagrodzenie = pensja
        # zwracamy gotową instancję
        return prac

    def __str__(self):
        """Zwraca reprezentację Pracownika jako str"""
        return '{} {} stanowisko: {}'.format(self.__imie, self.__nazwisko, self.__stanowisko)

    def __del__(self):
        """Wlasna implementacja dla usuwania obiektu"""
        print('Pracownik {} {} zostal usunięty'.format(self.__imie, self.__nazwisko))
        Pracownik.liczba_pracownikow -= 1
        print('Aktualna liczba pracowników:'.format(Pracownik.liczba_pracownikow))
