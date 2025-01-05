class Singleton:
    __instance = None  # _privatni

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.name = "Muj Singleton"



class DemoSingleton:
    def __init__(self):
        pass

if __name__ == "__main__":
    s = DemoSingleton()
    s1 = Singleton()
    s2 = Singleton()
    print(f"{s1}\n{s2}")
    print(bool(s1 is s2))
    pass
