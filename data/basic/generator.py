from faker import Faker
from data.basic.model_dataclasses import Person
import random


def generate_people(n: int, male_ratio: float = 0.5,
                    locale: str = "en_US") -> list[Person]:
    people = []
    fake = Faker(locale)
    Faker.seed(0)
    for i in range(n):
        male = random.random() < male_ratio
        person = Person(
            f"P-{str(i + 1).zfill(6)}",
            fake.name_male() if male else fake.name_female(),
            random.randint(18, 100),
            male)

        if male:
            person = Person(
                f"P-{str(i + 1).zfill(6)}",
                fake.name_male() if male else fake.name_female(),
                random.randint(18, 100),
                male)
        people.append(person)

    return people


if __name__ == "__main__":
    for person in generate_people(10, male_ratio=0.3,
                                  locale="es_ES"):
        print(person)
