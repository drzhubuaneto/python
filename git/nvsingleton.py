class Settings:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super (Settings,cls).__new__(cls)
        return cls.__instance
    
    def __init__(self, resolution, volume, language):
        if not hasattr(self, '_initialized'):
            self._resolution = resolution
            self._volume = volume
            self._language = language
            self._initialized = True 

    def __str__(self):
        return f"Resolution is {self._resolution}, volume is set on {self._volume}, and language is {self._language}"


if __name__ == "__main__":
    settings = Settings(1920, 20, "en")
    print(settings)

    settings2 = Settings(1000, 10, "cz")
    print(settings2)
