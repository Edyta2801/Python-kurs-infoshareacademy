"""
Wymagania:
napisz dwie klasy: Kon, Osiol, dziedziczące po klasie Zwierze (wykorzystaz zadanie_3 z poprzedniego dnia)

Nastepnie stworz klasy:
- Mul - dziedziczącą po Koniu i Ośle
- Oslomul - dziedziczącą po Ośle i Koniu

"""
import random

from code.Day_9.Zadanie_3_odpowiedz import Ssak


class Kon(Ssak):
    # barwa = "gniady"

    def __init__(self, barwa="gniady", gatunek="", waga_w_kg=None):
        super().__init__(gatunek, waga_w_kg)
        self.barwa = barwa
        if waga_w_kg is None:
            self.waga_w_kg = random.randint(100, 700)
        else:
            self.waga_w_kg = waga_w_kg


class Osiol(Ssak):
    def __init__(self, barwa="szarobury", gatunek="", waga_w_kg=None):
        super().__init__(gatunek, waga_w_kg)
        self.barwa = barwa
        if waga_w_kg is None:
            self.waga_w_kg = random.randint(100, 200)
        else:
            self.waga_w_kg = waga_w_kg


class Mul(Kon, Osiol):
    rodzenie_potomstwa = None

    def __init__(self, gatunek="Muł"):
        super().__init__()
        self.gatunek = gatunek


    def rodz_potomstwo(self, **kwargs):
        return "BEZPŁODNY"


class Oslomul(Osiol, Kon):
    rodzenie_potomstwa = None

    def __init__(self, gatunek="Oslomulica"):
        super().__init__()
        self.gatunek = gatunek

    def rodz_potomstwo(self, **kwargs):
        return "BEZPŁODNY"


konik = Kon(barwa="kary", gatunek="Arab")
osiolek = Osiol(barwa="szary", gatunek="Europejski")

print("konik:")
print(konik.barwa)
print(konik.gatunek)
print(konik.tryb_zycia)
print(konik.habitat)
print(konik.rodz_potomstwo())

print(80 * "#")

print("osiolek:")
print(osiolek.barwa)
print(osiolek.gatunek)
print(osiolek.tryb_zycia)
print(osiolek.habitat)
print(osiolek.rodz_potomstwo())

print(80 * "#")

mulica = Mul()
print("Muł:")
print(mulica.barwa)
print(mulica.gatunek)
print(mulica.tryb_zycia)
print(mulica.habitat)
print(mulica.rodz_potomstwo())

print(80 * "#")

oslomulica = Oslomul()
print("Osłomuł:")
print(oslomulica.barwa)
print(oslomulica.gatunek)
print(oslomulica.tryb_zycia)
print(oslomulica.habitat)
print(oslomulica.rodz_potomstwo())
