"""
Wymagania:
Napisz funkcję, sprawdzającą czy dana liczba jest w podanym zakresie liczb.

1. Weź pod uwagę zakres jako przekazywaną kolekcję (listę)
2. Weż pod uwagę zakres jako range(liczba)

Nie zapomnij o dokumentacji
Przygotuj zestaw danych testowych
"""

def eleganckie_zdanie(boolean):
    """
    Tworzy zdanie twierdzące lub zaprzeczenie
    zależnie od prawdziwości parametru boolean

    (boolean) -> (string)
    :param boolean:
    :return: string
    """
    nie = ""
    if not boolean:
        nie = "nie "
    return f"Podana liczba {nie}jest w zakresie."

def if_in_range_1(number, list_of_numbers):
    """
    Sprawdza czy podana liczba (number) jest w podanej kolekcji (list_of_numbers)

    (int, list) -> boolean
    :param number:
    :param list_of_numbers:
    :return: boolean
    """
    return number in list_of_numbers

def if_in_range_2(number, range_of_numbers):
    """
    Sprawdza czy podana liczba (number) jest w podanej zakresie (range_of_numbers)

    (int, range(int)) -> boolean
    :param number:
    :param range_of_numbers:
    :return: boolean
    """
    return number in range_of_numbers

def if_in_range_3(number, range_of_numbers_in_tuple_form):
    """
    Sprawdza czy podana liczba (number) jest w podanej zakresie (range_of_numbers_in_tuple_form)

    (int, tuple) -> boolean
    :param number:
    :param range_of_numbers_in_tuple_form:
    :return: boolean
    """
    return number in range(*range_of_numbers_in_tuple_form)

if __name__ == '__main__':

    # Sprawdzamy funkcję if_in_range_1
    print("Sprawdzanie funkcji if_in_range_1: (happy path)")
    print(eleganckie_zdanie(if_in_range_1(1, [1, 2, 3])))
    print()

    print("Sprawdzanie funkcji if_in_range_1: (negative)")
    print(eleganckie_zdanie(if_in_range_1(5, [1, 2, 3])))
    print()

    # Sprawdzamy funkcję if_in_range_2
    print("Sprawdzanie funkcji if_in_range_2: (happy path)")
    print(eleganckie_zdanie(if_in_range_2(1, range(8))))
    print()

    print("Sprawdzanie funkcji if_in_range_2: (negative)")
    print(eleganckie_zdanie(if_in_range_2(5, range(3))))
    print()

    # Sprawdzamy funkcję if_in_range_3
    print("Sprawdzanie funkcji if_in_range_3: (happy path)")
    print(eleganckie_zdanie(if_in_range_3(1, (1, 4))))
    print()

    print("Sprawdzanie funkcji if_in_range_3: (negative)")
    print(eleganckie_zdanie(if_in_range_3(5, (1, 4))))
    print()

