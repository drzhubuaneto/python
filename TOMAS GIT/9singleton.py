class Singleton:
    __instance = None # Privatni atribut, ktery drzi instanci tridy

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton,cls).__new__(cls)
        return cls.__instance
    
    def __init__(self):
        self.name="Muj singleton"

class DemoSingleton:
    def __init__(self):
        pass

if __name__=="__main__":
    # s=DemoSingleton()
    s1=Singleton()
    s2=Singleton()
    print(f"{s1}\n{s2}")
    print(bool(s1 is s2))
    pass
