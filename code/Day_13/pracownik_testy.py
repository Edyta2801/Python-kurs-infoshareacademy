from unittest import TestCase
from pracownik import Pracownik
from test_helper import Helpers


class PracownikTesty(TestCase):
    """Klasa testów naszej klasy Pracownik"""

    def setUp(self):
        """Metoda wywoływana przed każdym testem
        W niej możemy konfigurować wspólne cechy testów.
        Warto to robić tu, bo każdy test otrzyma świeże dane
        """
        # definiujemy dane wspólne dla testów
        self.imie = 'Jan'
        self.nazwisko = 'Nowak'
        self.p = Pracownik(self.imie, self.nazwisko)

    def tearDown(self):
        """Ta metoda jest uruchamiana po każdym teście
        W niej możemy czyścić dane, no. zamykać pliki"""
        self.p = None

    def test_konstruktor(self):
        """Test konstruktora klasy Pracownik"""
        self.assertIsNotNone(self.p)

    def test_stanowisko_get(self):
        """Test property stanowisko"""
        self.p.stanowisko = 'aktor'
        self.assertEqual(self.p.stanowisko, 'Aktor')

    def test_nazwisko_get(self):
        """Test dla metody nazwisko_get()"""
        oczekiwane_naz = self.nazwisko.upper()
        otrzymane_naz = self.p.nazwisko_get()
        self.assertEqual(otrzymane_naz, oczekiwane_naz )

    def test_wypisz_imie(self):
        """Test dla metody wypisz_imie()"""

        # x = funkcja()     -> użycie z nawiasami wykona funkcję
        # x = funkcja       -> użycie bez nawiasów - przypisyje funkcję do zmiennej
        # x()               -> możemy wywołać x jak funkcję - z nawiasami !!!

        # zapisujemy funkcję do zmiennej, nie używamy nawiasów
        funkcja_testowana = self.p.wypisz_imie

        # korzystamy z naszej funkcji pomocniczej
        otrzymany_output = Helpers.get_print_output(funkcja_testowana)
        oczekiwany_out = self.imie + '\n'

        self.assertEqual(otrzymany_output, oczekiwany_out)







