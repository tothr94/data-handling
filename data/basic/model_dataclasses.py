from dataclasses import dataclass, field
from functools import total_ordering


@dataclass(unsafe_hash=True)
@total_ordering
class Person:
    id: str = field(hash=True)
    name: str = field(compare=False)
    age: int = field(compare=False)
    male: bool = field(compare=False,
                       default=True)

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return NotImplemented

        return self.id < o.id

@dataclass(unsafe_hash=True)
class Car:
    plate: str = field(hash=True)
    type: str = field(compare=False)
    year: int = field(compare=False)
    automatic: bool = field(compare=False, default=True)

@dataclass(unsafe_hash=True)
class Airport:
    code: str = field(hash=True)
    name: str = field(compare=False)
    city: str = field(compare=False)
    state: str = field(compare=False)
    country: str = field(compare=False)


if __name__ == "__main__":
    p1 = Person("ABC", "Aladár", 16, True)
    p2 = Person("ABC", "Aladár2", 16)

    print(p1)
    print(p2)
    print(p1 == p2)
    print(p1 < p2)

    people = set()
    people.add(p1)
