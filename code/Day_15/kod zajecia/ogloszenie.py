class Ogloszenie(object):
    """Definiuje ogłoszenie o sprzedaży nieruchomości"""

    def __init__(self, opis, link):
        """Tworzy ogłoszenie"""
        self.opis = self.__formatuj_opis(opis)
        self.link = link

    def __formatuj_opis(self, opis):
        """Formatuje opis aby był ładny"""
        o = str(opis).split('\n')
        return ' '.join(o).strip()

    @staticmethod
    def zapisz_ogloszenia(nazwa_pliku, lista):
        """
        Zapisuje listę ogłoszeń do pliku
        :param nazwa_pliku: Nazwa pliku wyjściowego, str
        :param lista: Lista ogłoszeń, List
        :return: None
        """
        import pickle
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(lista, plik)

    @staticmethod
    def wczytaj_ogloszenia(nazwa_pliku):
        """
        Odczytuję listę ogłoszeń z pliku
        :param nazwa_pliku: Nazwa pliku z ogłoszeniami, str
        :return: Lista ogłoszeń, List
        """
        import pickle
        with open(nazwa_pliku, 'rb') as plik:
            return pickle.load(plik, encoding='utf-8')