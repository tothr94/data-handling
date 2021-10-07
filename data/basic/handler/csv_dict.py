import csv
import os

from data.basic import generator
from data.basic.model_dataclasses import Person


def write_people(people: list[Person],
                 path: str,
                 file_name: str = "people",
                 extension: str = ".csv",
                 heading: bool = True,
                 delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension), "w",
              newline="\n") as file:
        writer = csv.DictWriter(file, delimiter=delimiter,
                    fieldnames=["id", "name", "age", "male"])
        if heading:
            writer.writeheader()
        for person in people:
            writer.writerow(person.__dict__)

def read_people(path: str,
                 file_name: str = "people",
                 extension: str = ".csv",
                 delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name + extension),
              newline="\n") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        people = []
        for row in rows:
            people.append(
                Person(row["id"], row["name"], int(row["age"]),
                       bool(row["male"]))
            )
        return people

if __name__ == "__main__":
    p = Person("P-00000", "Teszt Elek", 16, True)
    print(p.__dict__)

    people = generator.generate_people(10)
    write_people(people, "C:/hallgato")
    people = read_people("C:/hallgato")
    for person in people:
        print(person)
    res = [print(person) for person in read_people("C:/hallgato")]
    print(res)