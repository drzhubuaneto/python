import os
import random

import pandas


def generatorAuta(cars):
    for i in range(len(cars)):
        yield f"Značka: {cars["brand"][i]}, Cena: {cars["price"][i]}, Motor: {cars["engine"][i]}, transmission: {cars["transmission"][i]}"


class iter_Auta:
    def __init__(self, cars):
        self.cars = cars
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > len(self.cars):
            raise StopIteration
        print(
            f"Značka: {self.cars["brand"][self.current]}, Cena: {self.cars["price"][self.current]}, Motor: {self.cars["engine"][self.current]}, transmission: {self.cars["transmission"][self.current]}"
        )
        self.current += 1


def nacti_csv(path):
    with open(path) as f:
        file = pandas.read_csv(f)
        file = file.to_dict()

    return file


def write_csv(path, list):
    df = pandas.DataFrame(list)
    df.to_csv(path, index=False)


def unikatni_hotnoty(dict):
    unikatni_dict = {}
    for item in dict:
        lt = []
        for i in range(len(dict[item])):
            lt.append(dict[item][i])
        lt = list(set(lt))
        unikatni_dict[item] = lt
    return unikatni_dict


def new_cars(dict, N):
    new_cars_list = []
    for i in range(N):
        car = {
            "brand": random.choice(dict["brand"]),
            "price": random.choice(dict["price"]),
            "engine": random.choice(dict["engine"]),
            "transmission": random.choice(dict["transmission"]),
        }
        new_cars_list.append(car)
    return new_cars_list


if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    file_path = os.path.join(dir, "data", "cars.csv")

    cars = nacti_csv(file_path)
    unikatni_dict = unikatni_hotnoty(cars)

    new_cars_list = new_cars(unikatni_dict, 5)

    new_file = os.path.join(dir, "data", "new_cars.csv")
    write_csv(new_file, new_cars_list)

    new_cars_list_file = nacti_csv(new_file)

    iterator0 = iter(iter_Auta(new_cars_list_file))

    print()

    next(iterator0)
    next(iterator0)
    next(iterator0)

    print()

    generator0 = generatorAuta(new_cars_list_file)

    print(next(generator0))
    print(next(generator0))
    print(next(generator0))

    pass
