from utils import write_file
from itertools import repeat
import student
import os
import xlrd

users_groups = {}


def student_add_group(group, data):
    if group not in users_groups:
        users_groups[group] = []
        users_groups[group].append(data)
    else:
        users_groups[group].append(data)


def generate_students_file():
    for group, students in users_groups.items():
        write_file(students, f"groups/{group}.csv")


def generete_students_collection(loc: str):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(1, sheet.nrows):
        *student_data, group = student.Student(sheet, i).getData()
        student_data.extend(repeat("", 12))
        student.users.append(student_data)
        student_add_group(group, student_data)
    else:
        generate_students_file()
        print("Successfull generated students files!")
        write_file(student.users[1:], "students.csv")


def main():

    if not os.path.exists("groups"):
        os.mkdir("groups")

    loc = input("Enter csv file path: ")

    if os.path.isfile(loc) == False:
        print("This path not correct!",
              "Press esc key close app and reopen!", sep="\n")
    else:
        generete_students_collection(loc)

    os.system("pause")


if __name__ == '__main__':
    main()
