import json
import os

from data.basic import generator
from data.basic.model_dataclasses import Person, Car


def write_people(people: list[Person],
                 path: str,
                 file_name: str = "people",
                 extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([person.__dict__ for person in people], file,
                  indent=2 if pretty else 0)


def write_cars(cars: list[Car],
               path: str,
               file_name: str = "cars",
               extension: str = ".json",
               pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([car.__dict__ for car in cars], file,
                  indent=2 if pretty else 0)


def read_people(path: str,
                file_name: str = "people",
                extension: str = ".json") -> list[Person]:
    with open(os.path.join(path, file_name + extension)) as file:
        people = []
        objects = json.load(file)
        for obj in objects:
            # obj.keys()
            person = Person(obj["id"], obj["name"], obj["age"],
                            obj["male"])
            people.append(person)
        return people

        """
        return [Person(obj["id"], obj["name"], obj["age"],
               obj["male"])
        for obj in json.load(file)]
        """


def read_cars(path: str,
              file_name: str = "cars",
              extension: str = ".json") -> list[Car]:

    with open(os.path.join(path, file_name + extension)) as file:
        return [Car(obj["plate"], obj["type"], obj["year"],
                    obj["automatic"])
                for obj in json.load(file)]


if __name__ == "__main__":
    write_people(generator.generate_people(10), "C:/hallgato",
                 pretty=True)
    write_cars(generator.generate_cars(20), "C:/hallgato",
               pretty=True)
    for person in read_people("C:/hallgato"):
        print(person)

    for car in read_cars("C:/hallgato"):
        print(car)
