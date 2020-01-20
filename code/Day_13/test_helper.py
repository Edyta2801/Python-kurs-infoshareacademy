import io
from contextlib import redirect_stdout


class Helpers(object):
    """Klasa z przydatnymi narzedziami"""

    @staticmethod
    def get_print_output(funkcja):
        """
        Przechwytuje wydruk z funkcji uzywajacej print()
        :param funkcja: (function)
        :return: str
        """
        # tworzymu bufor w pamięci do przechowywania
        # wartości string
        memory_buffer = io.StringIO()

        # przekierowujemy standardowy output do buforu
        with redirect_stdout(memory_buffer):
            # wywołujemy funkcję przekazaną w argumencie
            funkcja()
            # zwracamy string z zawartościa naszego bufora
            return memory_buffer.getvalue()

