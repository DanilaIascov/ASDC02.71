import csv
import time
from random import shuffle
from src.student import Student


def prepare_data(to_shuffle: bool = False) -> list:
    reader = csv.DictReader
    data = list(Student.reading_from_stream('data/students_data.csv', reader))
    if to_shuffle:
        shuffle(data)
    return data


def make_timer(callback, *args):
    start = time.perf_counter_ns()
    res = callback(*args)
    end = time.perf_counter_ns()
    print('Fail!', end=' ') if res is None else print('Success! ', end=' ')
    print(f"Spent time {end - start} ns")


if __name__ == '__main__':
    students = prepare_data()
    for student in students:
        print(student)
    Student.writing_in_stream(students[0], 'data/check_write_method.csv', csv.DictWriter)