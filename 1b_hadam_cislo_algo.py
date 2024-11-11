import random

low, high = 0, 100
attempts = 0
target_number = random.randint(low, high)
print(f"\nAlgoritmus hádá číslo {target_number} v rozmezí 0 až 100.")

while True:
    attempts += 1
    guess = (low + high) // 2
    print(f"Algoritmus hádá: {guess}")
        
    if guess < target_number:
        print("Nápověda: Skutečné číslo je větší.")
        low = guess + 1
    elif guess > target_number:
        print("Nápověda: Skutečné číslo je menší.")
        high = guess - 1
    else:
        print(f"Algoritmus uhodl číslo {target_number} na {attempts}. pokus.")
        break

#user_guess_game() #spustim hru pro uzivatele
#fast_guess_game() #spustim algoritmus
#napisu takto na zacatek:
#import random
#def user_guess_game():
    #odradkuju si to cely o jedno jakoby aby to bylo pod hrou pro uzivatele
#def fast_guess_game():
    #odradkuju algoritmus