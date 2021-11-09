import json
import os

from data.basic import generator
from data.basic.model_dataclasses import Person, Car, Airport

def write_people(people: list[Person],
                 path: str,
                 file_name: str = "people",
                 extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([person.__dict__ for person in people], file,
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


def write_cars(cars: list[Car],
               path: str,
               file_name: str = "cars",
               extension: str = ".json",
               pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([car.__dict__ for car in cars], file,
                  indent=2 if pretty else 0)


def read_cars(path: str,
              file_name: str = "cars",
              extension: str = ".json") -> list[Car]:
    with open(os.path.join(path, file_name + extension)) as file:
        return [Car(obj["plate"], obj["type"], obj["year"],
                    obj["automatic"])
                for obj in json.load(file)]


def write_airports(airports: list[Airport],
                   path: str, file_name: str = "airports",
                   extension: str = ".json",
                   pretty=True) -> None:
    file_name = file_name if file_name is not None else "airports"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([airport.__dict__ for airport in airports], file, indent=2 if pretty else None)


def read_airports(path: str,
                  file_name: str = "airports",
                  extension: str = ".json") -> list[Airport]:
    file_name = file_name if file_name is not None else "airports"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension)) as file:
        return [Airport(doc["name"], doc["code"], doc["city"], doc["state"], doc["country"])
                for doc in json.load(file)]


if __name__ == "__main__":
    write_people(generator.generate_people(10), "C:/hallgato",
                 pretty=True)
    write_cars(generator.generate_cars(20), "C:/hallgato",
               pretty=True)
    for person in read_people("C:/hallgato"):
        print(person)

    for car in read_cars("C:/hallgato"):
        print(car)
