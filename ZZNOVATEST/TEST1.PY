import os

# Načtení abecedy ze souboru
# Soubor alphabet.txt obsahuje každé písmeno na jednom řádku a končí středníkem

def nacti_abecedu(soubor):
    try:
        with open(soubor, 'r', encoding='utf-8') as f:
            abeceda = [radek.strip() for radek in f if radek.strip() != ';']
        return abeceda
    except FileNotFoundError:
        print("Soubor s abecedou nebyl nalezen.")
        exit(1)

# Funkce pro šifrování Caesarovou šifrou
def sifruj_text(text, klic, abeceda):
    vysledek = ""
    for znak in text:
        if znak in abeceda:
            pozice = abeceda.index(znak)
            nova_pozice = (pozice + klic) % len(abeceda)
            vysledek += abeceda[nova_pozice]
        elif znak == " ":
            vysledek += " "
        else:
            print(f"Nepodporovaný znak: {znak}")
            return None
    return vysledek

# Funkce pro dešifrování Caesarovou šifrou
def desifruj_text(text, klic, abeceda):
    return sifruj_text(text, -klic, abeceda)

# Funkce pro zpracování souboru (šifrování nebo dešifrování)
def zpracuj_soubor(soubor, klic, abeceda, desifrovani=False):
    try:
        with open(soubor, 'r', encoding='utf-8') as f:
            obsah = f.read()
        if desifrovani:
            vysledek = desifruj_text(obsah, klic, abeceda)
        else:
            vysledek = sifruj_text(obsah, klic, abeceda)
        if vysledek is None:
            return

        # Rozdělení názvu souboru a přípony
        jmeno, pripona = os.path.splitext(soubor)
        novy_soubor = jmeno + ("_decrypted" if desifrovani else "_encrypted") + pripona

        with open(novy_soubor, 'w', encoding='utf-8') as f:
            f.write(vysledek)
        print(f"Výsledek byl uložen do souboru: {novy_soubor}")
    except FileNotFoundError:
        print("Soubor nebyl nalezen.")

# Hlavní program
def hlavni():
    abeceda_soubor = r"ZZNOVATEST\alphabet.txt" "
    abeceda = nacti_abecedu(abeceda_soubor)

    while True:
        print("\nVyberte možnost:")
        print("1 - Šifrovat text")
        print("2 - Dešifrovat text")
        print("3 - Šifrovat soubor")
        print("4 - Dešifrovat soubor")
        print("5 - Konec")

        volba = input("Zadejte volbu: ")

        if volba == "1":
            text = input("Zadejte text k zašifrování: ")
            klic = int(input("Zadejte klíč: "))
            vysledek = sifruj_text(text, klic, abeceda)
            if vysledek is not None:
                print(f"Zašifrovaný text: {vysledek}")

        elif volba == "2":
            text = input("Zadejte text k dešifrování: ")
            klic = int(input("Zadejte klíč: "))
            vysledek = desifruj_text(text, klic, abeceda)
            if vysledek is not None:
                print(f"Dešifrovaný text: {vysledek}")

        elif volba == "3":
            soubor = input("Zadejte název souboru k zašifrování: ")
            klic = int(input("Zadejte klíč: "))
            zpracuj_soubor(soubor, klic, abeceda)

        elif volba == "4":
            soubor = input("Zadejte název souboru k dešifrování: ")
            klic = int(input("Zadejte klíč: "))
            zpracuj_soubor(soubor, klic, abeceda, desifrovani=True)

        elif volba == "5":
            print("Konec programu.")
            break

        else:
            print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
    hlavni()

