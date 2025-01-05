class Motor:
    def __init__(self, typ = None, objem = None, vykon = None):
        self.typ = typ
        self.objem = objem
        self.vykon = vykon

    def __str__(self):
        return f" typ: {self.typ}, objem {self.objem} l, vykon {self.vykon} koni"

class Karoserie:
    def __init__(self, typ = None, barva = None, pocet_dveri = None):
        self.typ = typ
        self.barva = barva
        self.pocet_dveri = pocet_dveri

    def __str__(self):
        return f" typ: {self.typ}, barva: {self.barva}, pocet dveri {self.pocet_dveri}"

class Vybava:
    def __init__(self):
        self.vycet = []
    
    def pridej_vybavu(self,prvek):
        self.vycet.append(prvek)
    
    def vycet_vybavy(self):
        return ", ".join(self.vycet)

    def __str__(self):
        return f" {self.vycet_vybavy()}"

class Kola:
    def __init__(self, velikost = None, typ = None):
        self.velikost = velikost
        self.typ = typ 

    def __str__(self):
        return f" velikost: {self.velikost}, typ: {self.typ}"

class Auto:
    def __init__(self):
        self.motor = None
        self.karoserie = None
        self.vybava = Vybava()
        self.kola = None

    def __str__(self):
        return f"""Vozidlo má motor: {self.motor}, Karaserie je typu {self.karoserie},
                    vybavu to ma {self.vybava} a kola {self.kola}"""
    
class Builder_Auto:
    def __init__(self):
        self.auto = Auto()

    def pridej_Motor(self, typ, objem, vykon):
        self.auto.motor = Motor(typ, objem, vykon)
        return self
    
    def pridej_Karoserii(self, typ, barva, pocet_dveri):
        self.auto.karoserie = Karoserie(typ, barva, pocet_dveri)
        return self

    def pridej_Vybavu(self, vybava):
        self.auto.vybava.pridej_vybavu(vybava)
        return self

    def pridej_Kola(self, velikost, typ):
        self.auto.kola = Kola(velikost, typ)
        return self
    
    def build(self):
        return self.auto
    
if __name__ == "__main__":
    builder = Builder_Auto()
    print()

    moje_auto = (builder
                 .pridej_Motor("benzin", 1.6, 150)
                 .pridej_Karoserii("sedan", "modrá", 5)
                 .pridej_Vybavu("klimatizace")
                 .pridej_Vybavu("navigace")
                 .pridej_Vybavu("střešní okno")
                 .pridej_Kola(50, "alu")
                 .build())
    print(moje_auto)
