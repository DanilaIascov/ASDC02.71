import csv
import json
from random import shuffle

from src.entity.student import Student


def prepare_data(to_shuffle: bool = False) -> list:
    reader = csv.DictReader
    data = Student.read_from_stream(reader=reader, filename='data/students_data.csv')
    if to_shuffle:
        shuffle(data)
    return data


if __name__ == '__main__':
    students = prepare_data()

    Student.write_in_stream(students, csv.DictWriter, 'data/check_write_method.csv')
    Student.write_in_stream([students[0]], json.dump, 'data/check_write_method.json')
    Student.write_in_stream([students[0]])
