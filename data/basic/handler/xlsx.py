import openpyxl
from openpyxl import Workbook

from data.basic import generator
from data.basic.model_dataclasses import Person


def write_people(people: list[Person],
                 workbook: openpyxl.Workbook,
                 sheet_name: str = "people"):
    sheet = workbook.create_sheet(sheet_name)
    for row in range(len(people)):
        sheet.cell(row=row + 1, column=1, value=people[row].id)
        sheet.cell(row=row + 1, column=2, value=people[row].name)
        sheet.cell(row=row + 1, column=3, value=people[row].age)
        sheet.cell(row=row + 1, column=4, value=people[row].male)


def read_people(workbook: openpyxl.Workbook,
                 sheet_name: str = "people") -> list[Person]:
    sheet = workbook[sheet_name]

    people = []
    row = 1
    # for row in range(1, 11):
    while True:
        if sheet.cell(row=row, column=1).value is None:
            break
        person = Person(
            sheet.cell(row=row, column=1).value,
            sheet.cell(row=row, column=2).value,
            int(sheet.cell(row=row, column=3).value),
            bool(sheet.cell(row=row, column=4).value)
        )
        row += 1
        people.append(person)
    return people

if __name__ == "__main__":
    wb = Workbook()
    # wb = openpyxl.load_workbook("C:/hallgato/data.xlsx")
    write_people(generator.generate_people(20), wb)
    for person in read_people(wb):
        print(person)
    wb.save("C:/hallgato/data.xlsx")
