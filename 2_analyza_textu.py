import re
from collections import Counter


def load_txt():
    f = open('2text.txt', 'r')
    f = f.read()
    return f

def pocitani_slov(file):
    string = file
    words = string.split(' ')
    print(f"pocet slov v souboru je {len(words)}")

def pocitani_vet(file):
    string = file
    sent = string.split('.')
    print(f"pocet vet v souboru je {len(sent)}")
    
def pocitani_odst(file):
    string = file
    odst = string.split('\n')
    print(f"pocet odstavcu v souboru je {len(odst)}")

def frekvence(file, n):
    soubor = open("Employees.txt", "w") 
    clean_string = re.sub(r"[^\w']+", " ", file)
    clean_string = clean_string.lower()
    slova = clean_string.split(' ') #mam rozdeleno na prvky = je to list rn
    li = Counter(slova)
    slovnik = dict(li)
    razeni = sorted(slovnik.items(), key=lambda item: item[1], reverse=True)
    for i in range(n):
        print(f"{razeni[i][0]} se vyskytuje {razeni[i][1]}")
        name = f"{razeni[i][0]} se vyskytuje {razeni[i][1]}"
        soubor.write(name) 
        soubor.write("\n") 
    soubor.close() 
    print("Data is written into the file.") 

    pass
    

if __name__ == "__main__": #vytvorim main
    file = load_txt() #funkce takze ()
    pocitani_slov(file)
    pocitani_vet(file)
    pocitani_odst(file)
    frekvence(file, 3)
    pass