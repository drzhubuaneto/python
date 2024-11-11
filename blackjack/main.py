from Dealer import dealer_logika
from Generovani_balicku import priprav_hru
from rozdani_karet import dalsi_karta, nacteni_karet, zakladni_rozdani
from Spocitani_hodnoty_karet import hodnoty_karet, uprava_hodnoty
from zobrazeni_karet import zobrazeni

if __name__ == "__main__":
    print()
    balicek = priprav_hru()
    nacteni_karet(balicek)
    konto_hrace = 1000
    while True:
        hrac, dealer = zakladni_rozdani()
        zobrazeni("hrac", hrac)
        hrac_hodnota, eso_hrac = hodnoty_karet(hrac)
        print(f"Hodnota karet hrece je {hrac_hodnota}")
        zobrazeni("dealer", dealer, True)
        akce = ""
        sazka = 0

        while True:
            if sazka == 0:
                sazka = int(input("Zadej sazku: "))

            ukon = input("Zvol ukon dalsi: hit, stay - ")
            match ukon:
                case "hit":
                    hrac.append(dalsi_karta())
                    zobrazeni("hrac", hrac)
                    hrac_hodnota, eso_hrac = hodnoty_karet(hrac)
                    print(f"Hodnota karet hrace je {hrac_hodnota}")

                    if hrac_hodnota == 21:
                        print("vyhral jsi")
                        akce = "vyhra"
                        break

                    if hrac_hodnota > 21 and eso_hrac is True:
                        hrac_hodnota = uprava_hodnoty(hrac_hodnota)
                        eso_hrac = False
                        print(f"Hodnota karet hrece je {hrac_hodnota}")

                    if hrac_hodnota > 21 and eso_hrac is False:
                        print("Prohral jsi")
                        akce = "prohra"
                        break

                case "stay":
                    print("Konec hry hrace")
                    break

                case _:
                    print("Tato volba bohužel není podporována")

        hodnota_dealer = dealer_logika(dealer)
        zobrazeni("deler", dealer)
        print(f"Hodnota dealera je {hodnota_dealer}")

        if akce == "vyhra":
            konto_hrace += sazka * 1.5

            print("beres penize")
        elif akce == "prohra":
            konto_hrace -= sazka
            print("ztracis penize")
        elif hodnota_dealer > 21:
            konto_hrace += sazka * 2
            print("dealer ma moc, beres penize")
        elif hodnota_dealer > hrac_hodnota:
            konto_hrace -= sazka
            print("dealer ma vice, prohravas")
        elif hodnota_dealer < hrac_hodnota:
            konto_hrace += sazka * 2
            print("mas vic nez dealer, vyhravas")

        print(f"Stav tveho konta je {konto_hrace}")
