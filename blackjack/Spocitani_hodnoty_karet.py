def hodnoty_karet(karty):
    suma = 0
    eso = False
    for i in range(len(karty)):
        if karty[i][1][0] == "Eso":
            suma += karty[i][1][1][1]
            eso = True
        else:
            suma += karty[i][1][1]

    return suma, eso


def uprava_hodnoty(hodnota):
    new_hodnota = hodnota - 10
    return new_hodnota
