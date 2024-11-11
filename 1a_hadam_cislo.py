import random

poc_cislo=random.randint(0,100)
pokusy=0

while True: #nezapomenout ze input vraci string = napis int (input("co chci aby mi to vypsalo na konzoli"))
    hrac_cislo=int (input("zadej cislo od 0 do 100: ")) #alt a sipky = hejbu si s celym radkem nahoru a dolu
    if 0<=hrac_cislo and hrac_cislo<=100:
        pokusy += 1 #kdyz zada cislo zacne pocitat pokusy (proste vzdy kdyz cyklus dojde k zadani dalsiho cisle pripocte 1)
        if hrac_cislo > poc_cislo:
            print("tvoje cislo je vetsi nez pocitacovo cislo",end='') #,end='' tak mi to neodradkuje automaticky            
        elif hrac_cislo < poc_cislo:
            print("tvoje cislo je mensi nez pocitacovo cislo") #kdyz tam end='' neni - automaticky odradkuje
        else:
            print(f"vyhral jsi! uhodl jsi cislo {poc_cislo} na {pokusy}. pokus") #formatovany string = (f"napisu co chci {promenna} jupijajou")
            break   
    else:
        print("zadej cislo od 0 do 100!")


pass
