"""
Wymagania:
Napisz funkcję odwaracjącą podanego stringa.
Nie zapomnij o dokumentacji
"""
def reverse_string(string):
    """
    Returns reversed string

    :param string:
    :return: string
    """
    return string[::-1]

if __name__ == '__main__':
    string = input("Podaj string: ")

    print("Wypisuję oryginalny string:")
    print(string)

    print("Wypisuję odwrócony string:")
    print(reverse_string(string))
