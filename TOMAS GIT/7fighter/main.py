from fight import Fight
from fighter import Fighter

if __name__=="__main__":
    f0=Fighter("Jirka Kara",25,30,40,20,10)
    f1=Fighter("Svarta",20,38,50,28,15)
    fight=Fight(f0,f1)
    fight.simulate()
