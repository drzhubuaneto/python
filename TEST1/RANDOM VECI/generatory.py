def simple_generator():
    print("Start")
    yield 1
    print("After yielding 1")
    yield 2
    print("After yielding 2")
    yield 3
    print("End of generator")


gen = simple_generator()

print(next(gen))  # 1. volání next()
print(next(gen))  # 2. volání next()
print(next(gen))  # 3. volání next()


#ITERATORY
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.cislo = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cislo += 2
        return self.cislo


print()
iterator0 = iter(EvenNumbers(6))
print(next(iterator0))

print(next(iterator0))
