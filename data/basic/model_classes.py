from functools import total_ordering


@total_ordering
class Person:
    id: str
    name: str
    age: int
    male: bool

    def __init__(self, id: str, name: str, age: int, male: bool = True) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.male = male

    def __str__(self) -> str:
        return "#{id}: {name} ({age}, {male})".format(
            id=self.id,
            name=self.name,
            age=self.age,
            male=self.male
        )

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Person) and self.id == o.id

    """
    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
    """

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.id < other.id

    def __hash__(self) -> int:
        return self.id.__hash__()


@total_ordering
class Car:
    plate: str
    type: str
    year: int
    automatic: bool

    def __init__(self, plate: str, type: str, year: int, automatic=True) -> None:
        self.plate = plate
        self.type = type
        self.year = year
        self.automatic = automatic

    def __str__(self) -> str:
        return "{plate} ({type}, {year}): {automatic}".format(
            plate=self.plate,
            type=self.type,
            year=self.year,
            automatic=self.automatic
        )

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Car) and self.plate == o.plate

    def __hash__(self) -> int:
        return self.plate.__hash__()

    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.plate < other.plate


@total_ordering
class Airport:
    code: str
    name: str
    city: str
    state: str
    country: str

    def __init__(self, code: str, name: str, city: str, state: str, country: str) -> None:
        self.code = code
        self.name = name
        self.city = city
        self.state = state
        self.country = country

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Airport) and self.code == o.code

    def __str__(self) -> str:
        return "{code} ({name}): {city}, {state}, {country}".format(
            code=self.code, name=self.name, city=self.city,
            state=self.state, country=self.country)

    def __hash__(self) -> int:
        return self.code.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Airport):
            return NotImplemented

        return self.code < o.code


if __name__ == "__main__":
    """
    p1.id = "123456AB"
    p1.name = "Teszt Elek"
    p1.age = 19
    p1.male = True
    """
    p1 = Person(id="123456AB", name="Teszt Elek", age=19)
    p2 = Person(id="123456AB1", name="Teszt Elek2", age=20, male=False)

    print(p1)
    print(p2)
    print(p1 == p2)
    print(p1 != p2)
    print(p1 <= p2)

    print("name".__hash__())
    print("name".__hash__())
    print("name".__hash__())
    print("alma".__hash__())
    print("namee".__hash__())
