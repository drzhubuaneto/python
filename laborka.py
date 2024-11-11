zkumavka = 0 #jedno = prirazuju hodnotu
max = 0 #kdyby min tak napisu 99999999999 cca

while True:
    sample_size=int (input("zadej mnozstvi vzorku ktere vkladas: "))
    zkumavka=zkumavka + sample_size
    #zkumavka+=sample_size #to samy co radek nad tim jen kratsi zapis
    if zkumavka >= 10:
        print("spravne poustim")
        break
    if zkumavka < 10:
        print(f"nedostatek vzorku, pridej {10-zkumavka}") #formatovany string (f a to v {promenna})

    if sample_size > max:
        max = sample_size
print(f"maximum je {max}")