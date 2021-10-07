import csv
import os

from data.basic import generator
from data.basic.model_dataclasses import Person, Car


def write_people(people: list[Person],
                 path: str,
                 file_name: str = "people.csv",
                 delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name), "w",
              newline="\n") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for person in people:
            writer.writerow([person.id, person.name,
                             person.age, person.male])

def read_people(path: str, file_name: str = "people.csv",
                delimiter: str = ";") -> list[Person]:
    with open(os.path.join(path, file_name)) as file:
        rows = csv.reader(file, delimiter=delimiter)
        people = []
        for row in rows:
            people.append(
                Person(row[0], row[1], int(row[2]),
                       bool(row[3]))
            )
        return people
        # return [Person(row[0], row[1], int(row[2]),
        #               bool(row[3])) for row in rows]


def write_cars(cars: list[Car],
               path: str,
               file_name: str = "cars.csv",
               delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name), "w",
              newline="\n") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for car in cars:
            writer.writerow([car.plate, car.type,
                             car.year, car.automatic])

if __name__ == "__main__":
    people = generator.generate_people(10)
    write_people(people, "C:/hallgato", file_name="emberek.csv")

    cars = generator.generate_cars(10)
    write_cars(cars, "C:/hallgato")

    people = read_people("C:/hallgato", file_name="emberek.csv")
    for person in people:
        print(person)