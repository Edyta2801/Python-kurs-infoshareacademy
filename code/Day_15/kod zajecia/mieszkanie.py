import requests
from bs4 import BeautifulSoup
from ogloszenie import Ogloszenie
import pickle

# lista ogłoszeń
ogloszenia = []

# adres strony
adres = 'https://www.otodom.pl/wynajem/mieszkanie/gdansk/oliwa/?search%5Bdescription%5D=1&search%5Bdist%5D=0&search%5Bdistrict_id%5D=16&search%5Border%5D=created_at_first%3Adesc&nrAdsPerPage=72'

# pobieramy zawartość strony
res = requests.get(adres)
res.raise_for_status()
# print(res.text)

# tworzymy zupę
soup = BeautifulSoup(res.text, 'html.parser')

# z zupy wybieramy interesujące nas elementy (listę):
# class='offer-item-header'
# znacznik <a> , który definiuje link
# zasada określona w selcect() - znacznik a znajduje się wew. atrybutu offer-item-header
ads = soup.select('.offer-item-header a')
# print(ads)

# elementy z listy są obrabiane i zapisywane jako obiekty Ogloszenie
# obiekt dodawany jest do listy
for ad in ads:
    # print(ad)
    # print(ad.getText())
    # print(ad.get('href'))
    # print('-----------------------')
    o = Ogloszenie(ad.getText(), ad.get('href'))
    print(o.opis)
    print(o.link)
    ogloszenia.append(o)

# zapisujemy listę obiektów do pliku
# dzięki temu nasze dane są trwałe - nie znikną po zakończeniu programu
Ogloszenie.zapisz_ogloszenia('ogleszenia.dat', ogloszenia)
# odczytujemy listę obiektów z pliku
ogloszenia_plik = Ogloszenie.wczytaj_ogloszenia('ogleszenia.dat')

# drukujemy wczytaną listę
for o in ogloszenia_plik:
    print(o.opis, o.link)

# pomysł na działanie programu:
# 1. otwieramy plik z ogłoszeniami, jeśli go nie ma to tworzymy
# 2. wczytujemy stronę
# 3. tworzymy zupę int wyszukujemy odpowiednie atrybuty
# 4. tworzymy obiekt, sprawdzamy czy nie ma już na liście
# 5. jeśli nie ma na liście to:
# 5a.   dodajemy do listy
# 5b.   dodajemy opis oraz link do treści wiadomości email
# 6. zapisujemy zaktualizowaną listę wszystkich ogłoszeń
# 7. wysyłamy email z nowymi ogłoszeniami

# program dodajemy do harmonogramu zadań, aby komputer samodzielnie wykonywał go










