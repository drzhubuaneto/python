from abc import ABC, abstractmethod


class hracka(ABC):
    def __init__(self, nazev, hmotnost, doporuceny_vek, popis):
        self.nazev = nazev
        self.hmotnost = hmotnost
        self.doporuceny_vek = doporuceny_vek
        self.popis = popis

    @abstractmethod
    def hraj_si(self):
        pass

    @abstractmethod
    def __str__(self):
        return f"Název hracky: {self.nazev}, hmotnost: {self.hmotnost}, doporuceny vek: {self.doporuceny_vek}, popis: {self.popis} "

class drevena_hracka(hracka):
    def __init__(self, nazev, hmotnost, doporuceny_vek, popis):
        super().__init__(nazev, hmotnost, doporuceny_vek, popis)

    def hraj_si(self):
        return "Hraju si s drevenou hrackou"
    
    def __str__(self):
        return "Jedna se o drevenou hracku: " + super().__str__()


class plastova_hracka(hracka):
    def __init__(self, nazev, hmotnost, doporuceny_vek, popis):
        super().__init__(nazev, hmotnost, doporuceny_vek, popis)

    def hraj_si(self):
        return "Hraju si s plastovou hrackou"
    
    def __str__(self):
        return "Jedna se o plastovou hracku: " + super().__str__()

class plysova_hracka(hracka):
    def __init__(self, nazev, hmotnost, doporuceny_vek, popis):
        super().__init__(nazev, hmotnost, doporuceny_vek, popis)

    def hraj_si(self):
        return "Hraju si s plysovou hrackou"
    
    def __str__(self):
        return "Jedna se o plysovou hracku: " + super().__str__()



class TovarnaHracky:
    @staticmethod
    def vyrob_hracku(typ, nazev, hmotnost, doporuceny_vek, popis):
        if typ == "drevena":
            return drevena_hracka(nazev, hmotnost, doporuceny_vek, popis)
        elif typ == "plastova":
            return plastova_hracka(nazev, hmotnost, doporuceny_vek, popis)
        elif typ == "plysova":
            return plysova_hracka(nazev, hmotnost, doporuceny_vek, popis)


if __name__ == "__main__":
    print()
    dreveny_mec = TovarnaHracky.vyrob_hracku("drevena", "Dřevěný měč", 1500, 7, "Dřevený měč co vám přelomí holeň dřív než aby se zlomil on")
    print(dreveny_mec)
    print(dreveny_mec.hraj_si())
    print()
    plastova_kachnicka = TovarnaHracky.vyrob_hracku("plastova", "Plastová kachnička", 200, 3, "Jste programátor a nemáte kamarády já jako kachnička jsem perfektní volba")
    print(plastova_kachnicka)
    print(plastova_kachnicka.hraj_si())
    print()
    plysovy_kamarad = TovarnaHracky.vyrob_hracku("plysova", "Plysovy kamarad", 500, 4, "Jste programátor a nestačí vám jenom kachnička kupte si mě")
    print(plysovy_kamarad)
    print(plysovy_kamarad.hraj_si())
