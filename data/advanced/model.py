from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import total_ordering


class Entity(ABC):
    @staticmethod
    @abstractmethod
    def collection_name():
        pass

    @staticmethod
    @abstractmethod
    def field_names():
        pass

    @staticmethod
    @abstractmethod
    def from_sequence(seq: list[str]):
        pass

    @abstractmethod
    def to_sequence(self):
        pass


@dataclass(unsafe_hash=True)
@total_ordering
class Person(Entity):
    id: str = field(hash=True)
    name: str = field(compare=False)
    age: int = field(compare=False)
    male: bool = field(compare=False,
                       default=True)

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return NotImplemented

        return self.id < o.id

    @staticmethod
    def collection_name():
        return "people"

    @staticmethod
    def field_names():
        return ["id", "name", "age", "male"]

    @staticmethod
    def from_sequence(seq: list[str]):
        return Person(seq[0], seq[1], int(seq[2]),
                      bool(seq[3]))

    def to_sequence(self):
        return [self.id, self.name, str(self.age),
                str(self.male)]


@dataclass(unsafe_hash=True)
class Car(Entity):
    plate: str = field(hash=True)
    type: str = field(compare=False)
    year: int = field(compare=False)
    automatic: bool = field(compare=False, default=True)

    @staticmethod
    def collection_name():
        return "cars"

    @staticmethod
    def field_names():
        return ["plate", "type", "year", "automatic"]

    @staticmethod
    def from_sequence(seq: list[str]):
        return Car(seq[0], seq[1], int(seq[2]), bool(seq[3]))

    def to_sequence(self):
        return [self.plate, self.type, str(self.year),
                str(self.automatic)]


@dataclass(unsafe_hash=True)
class Airport(Entity):
    code: str = field(hash=True)
    name: str = field(compare=False)
    city: str = field(compare=False)
    state: str = field(compare=False)
    country: str = field(compare=False)

    @staticmethod
    def collection_name():
        return "airports"

    @staticmethod
    def field_names():
        return ["code", "name", "city", "state", "country"]

    @staticmethod
    def from_sequence(seq: list[str]):
        return Airport(seq[0], seq[1], seq[2], seq[3], seq[4])

    def to_sequence(self):
        return [self.code, self.name, self.city, self.state, self.country]


if __name__ == "__main__":
    p = Person("x", "y", 1, False)
    print(p.collection_name())
    print(Person.collection_name())

    p = Person.from_sequence(["P-000", "Teszt Elek", "20", "True"])
    print(p)
    print(p.to_sequence())
    print(Person.field_names())
