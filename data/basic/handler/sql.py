from os import read

import mysql.connector
from mysql.connector import MySQLConnection

from data.basic import generator
from data.basic.model_dataclasses import Person, Car, Airport


def write_people(people: list[Person],
                 connection: MySQLConnection,
                 table_name: str = "people"):
    script = f"""
    CREATE TABLE {table_name} (
        id VARCHAR(8) NOT NULL PRIMARY KEY,
        name VARCHAR(50),
        age TINYINT,
        male BOOLEAN
    );
    """

    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    for _ in cursor.execute(script, multi=True):
        pass

    cursor.executemany(
        f"INSERT INTO {table_name} (id, name, age, male) VALUES (%s, %s, %s, %s)",
        [(person.id, person.name, person.age, person.male)
         for person in people]
    )
    connection.commit()
    cursor.close()


def read_people(connection: MySQLConnection,
                table_name: str = "people") -> list[Person]:
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    people = []
    for row in cursor.fetchall():
        people.append(Person(
            row[0], row[1], int(row[2]), bool(row[3])
        ))
    cursor.close()
    return people


def write_cars(cars: list[Car],
               connection: MySQLConnection,
               table_name: str = "cars") -> None:
    table_name = table_name if table_name is not None else "cars"
    script = """
    CREATE TABLE {table_name} (
        plate VARCHAR(20) NOT NULL PRIMARY KEY,
        type VARCHAR(20),
        year SMALLINT,
        automatic BOOLEAN
    );
     """.format(table_name=table_name)

    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    for _ in cursor.execute(script, multi=True):
        pass

    cursor.executemany(
        f"INSERT INTO {table_name} (plate, type, year, automatic) VALUES (%s, %s, %s, %s)",
        [(car.plate, car.type, car.year, car.automatic) for car in cars]
    )
    connection.commit()
    cursor.close()


def read_cars(connection: MySQLConnection,
              table_name: str = "cars") -> list[Car]:
    table_name = table_name if table_name is not None else "cars"
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    res = [Car(row[0], row[1], int(row[2]), bool(row[3])) for row in cursor.fetchall()]
    cursor.close()
    return res


def write_airports(airports: list[Airport],
                   connection: MySQLConnection,
                   table_name: str = "airports") -> None:
    table_name = table_name if table_name is not None else "airports"
    script = """
    CREATE TABLE {table_table_name} (
        code CHAR(4) NOT NULL PRIMARY KEY,
        name VARCHAR(100),
        city VARCHAR(50),
        state VARCHAR(50),
        country VARCHAR(50)
    );
     """.format(table_name=table_name)

    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    for _ in cursor.execute(script, multi=True):
        pass

    cursor.executemany(
        f"INSERT INTO {table_name} (code, name, city, state, country) VALUES (%s, %s, %s, %s, %s)",
        [(airport.code, airport.name, airport.city, airport.state, airport.country) for airport in airports]
    )
    cursor.close()
    connection.commit()


def read_airports(connection: MySQLConnection,
                  table_name: str = "airports") -> list[Airport]:
    table_name = table_name if table_name is not None else "airports"
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    res = [Airport(row[0], row[1], row[2], row[3], row[4]) for row in cursor.fetchall()]
    cursor.close()
    return res


if __name__ == "__main__":
    con = mysql.connector.connect(
        host="TODO",
        database="TODO",
        user="TODO",
        passwd="TODO"
    )

    write_people(generator.generate_people(1000), con)
    for person in read_people(con):
        print(person)
    con.close()
