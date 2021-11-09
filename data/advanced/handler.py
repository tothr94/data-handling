import csv
import os
from typing import Type

from data.advanced import generator
from data.advanced.model import Entity, Person, Car


class CSVHandler:
    @staticmethod
    def read(entity_type: Type[Entity],
             path: str,
             file_name: str = None,
             extension: str = ".csv",
             delimiter: str = ";"
             ) -> list[Entity]:

        if file_name is None:
            file_name = entity_type.collection_name()

        with open(os.path.join(
                path, file_name + extension
        ), newline="\n") as file:
            rows = csv.DictReader(file, delimiter=delimiter)
            entities = []
            for row in rows:
                seq = []
                for name in entity_type.field_names():
                    seq.append(row[name])
                entities.append(
                    entity_type.from_sequence(seq)
                )
            return entities


    @staticmethod
    def write(entities: list[Entity],
              path: str,
              file_name: str = None,
              extension: str = ".csv",
              delimiter: str = ";"):

        if file_name is None:
            file_name = entities[0].collection_name()

        with open(os.path.join(
            path, file_name + extension
        ), "w", newline="\n") as file:
            writer = csv.DictWriter(
                file, fieldnames=entities[0].field_names(),
            delimiter=delimiter)

            writer.writeheader()
            for entity in entities:
                writer.writerow(entity.__dict__)

if __name__ == "__main__":
    CSVHandler.write(generator.generate_people(10), "C:/hallgato")
    for person in CSVHandler.read(Person, "C:/hallgato"):
        print(person)

    CSVHandler.write(generator.generate_cars(10), "C:/hallgato")
    for person in CSVHandler.read(Car, "C:/hallgato"):
        print(person)