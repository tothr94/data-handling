from faker import Faker
from faker_airtravel import AirTravelProvider
from faker_vehicle import VehicleProvider

from data.advanced.model import Person, Car, Airport
import random


def generate_people(n: int, male_ratio: float = 0.5,
                    locale: str = "en_US",
                    unique: bool = False,
                    min_age: int = 0,
                    max_age: int = 100) -> list[Person]:
    assert n > 0
    assert 0 <= male_ratio <= 1
    assert min_age >= 0
    assert min_age <= max_age <= 100

    people = []
    fake = Faker(locale)
    # Faker.seed(0)
    fake = fake if not unique else fake.unique
    for i in range(n):
        male = random.random() < male_ratio
        person = Person(
            f"P-{str(i + 1).zfill(6)}",
            fake.unique.name_male() if male else fake.unique.name_female(),
            random.randint(min_age, max_age),
            male)

        people.append(person)

    return people


def generate_cars(n: int, automatic_ratio: float = 0.2,
                  locale: str = "hu_HU",
                  unique: bool = False,
                  min_year: int = 1950,
                  max_year: int = 2021) -> list[Car]:
    assert n > 0
    assert 0 <= automatic_ratio <= 1
    assert 1908 <= min_year
    assert min_year <= max_year <= 2021

    fake_plate = Faker(locale)
    fake_plate.add_provider(VehicleProvider)
    fake_plate = fake_plate if not unique else fake_plate.unique

    fake2 = Faker(locale)
    fake2.add_provider(VehicleProvider)
    cars = []
    for i in range(n):
        automatic = random.random() < automatic_ratio
        car = Car(
            fake_plate.license_plate(),
            fake2.vehicle_make(),
            random.randint(min_year, max_year),
            automatic
        )
        cars.append(car)
    return cars


def generate_airports(n: int, country: str = None,
                      city: str = None,
                      unique: bool = False,
                      attempts: int = None) -> list[Airport]:
    fake = Faker()
    fake.add_provider(AirTravelProvider)

    airports = []
    for i in range(n if attempts is None else attempts):
        values = fake.airport_object()
        airport = Airport(
            values["icao"],
            values["airport"],
            values["city"],
            values["state"],
            values["country"]
        )

        if len(airports) == n:
            break
        if unique and airport in airports:
            continue
        if country is not None and airport.country != country:
            continue
        if city is not None and airport.city != city:
            continue

        airports.append(airport)
    return airports


if __name__ == "__main__":
    """
    for person in generate_people(0, male_ratio=0.3,
                                  locale="es_ES", min_age=1, max_age=10):
        print(person)
    """
    """
    for car in generate_cars(100, locale="en_US", unique=True):
        print(car)
    """

    for airport in generate_airports(5, country="Germany",
                                     unique=True, attempts=10000):
        print(airport)
