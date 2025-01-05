from rozdani_karet import dalsi_karta
from Spocitani_hodnoty_karet import hodnoty_karet, uprava_hodnoty


def dealer_logika(karty: list):
    while True:
        hodnota, eso = hodnoty_karet(karty)
        if hodnota > 21 and eso is True:
            hodnota = uprava_hodnoty(hodnota)
            eso = False

        if hodnota >= 17:
            return hodnota
        else:
            karty.append(dalsi_karta())
