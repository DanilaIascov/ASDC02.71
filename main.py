import csv
import json
from random import shuffle

from ASDC_lab0.src.classes.student import Student


def prepare_data(to_shuffle: bool = False) -> list:
    reader = csv.DictReader
    data = Student.read_from_stream(filename='data/students_data.csv', reader=reader)
    if to_shuffle:
        shuffle(data)
    return data


if __name__ == '__main__':
    students = prepare_data()
    for student in students:
        print(student)
    Student.write_in_stream(students[0], 'data/check_write_method.json', json.dump)
