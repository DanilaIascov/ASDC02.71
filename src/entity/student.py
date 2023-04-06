import os.path

from src.entity.faculty import Faculty


class Student:
    """Class representing the entity of the student
    the class contains the following methods
    __init__()
    __copy__()
    assign()
    __eq__()
    read_from_stream()
    write_in_stream()

    """

    def __init__(
            self,
            firstname: str = 'empty',
            lastname: str = 'empty',
            faculty: str = 'None',
            year_of_birth: int = 0,
            year_of_enrollment: int = 0,
            idnp: int = 0
    ):
        """Student entity constructor

        :param firstname:
        :param lastname:
        :param faculty:
        :param year_of_birth:
        :param year_of_enrollment:
        :param idnp:
        """
        self.firstname = firstname
        self.lastname = lastname
        self.idnp = idnp
        self.year_of_enrollment = year_of_enrollment
        self.year_of_birth = year_of_birth
        self.faculty = Faculty.get_faculty_index(faculty)

    def __copy__(self) -> object:
        """Returns a copy of the object

        :return: object Student
        """
        copy_instance = Student(
            firstname=self.firstname,
            lastname=self.lastname,
            idnp=self.idnp,
            year_of_enrollment=self.year_of_enrollment,
            year_of_birth=self.year_of_birth,
            faculty=Faculty.get_faculty_name(self.faculty)
        )
        return copy_instance

    def assign(self, other) -> None:
        """Assignment operator overload

        :param other: object Student whose properties will be assigned to the current object
        """
        self.firstname = other.firstname
        self.lastname = other.lastname
        self.faculty = other.faculty
        self.year_of_birth = other.year_of_birth
        self.year_of_enrollment = other.year_of_enrollment
        self.idnp = other.idnp

    def __str__(self):
        return f'firstname:{self.firstname}, ' \
               f'lastname: {self.lastname}, ' \
               f'faculty: {Faculty.get_faculty_name(self.faculty)}, ' \
               f'year of birth: {self.year_of_birth}, ' \
               f'year of enrollment: {self.year_of_enrollment}, ' \
               f'idnp: {self.idnp}'

    def __eq__(self, other) -> bool:
        """comparison operator overload

        :param other:
        :return: True if object fields are equal otherwise False
        """
        if isinstance(other, Student):
            return self.firstname == other.firstname and \
                self.lastname == other.lastname and \
                self.faculty == other.faculty and \
                self.year_of_birth == other.year_of_birth and \
                self.year_of_enrollment == other.year_of_enrollment and \
                self.idnp == other.idnp
        return False

    @staticmethod
    def read_from_stream(reader, filename: str | None = None, data=None) -> list:
        """Method for reading from the stream

        :param reader: to read data from the file
        :param filename: the name of the file in which the data store
        :param data: to create an array of data not from a file
        :return: list of students
        """
        return StudentSerializer.read(reader, filename, data)

    @staticmethod
    def write_in_stream(array: list, writer=None, filename: str | None = None):
        """Method for writing in  the stream

        :param writer: to write data in the file
        :param array: data which will be written
        :param filename: the name of the file in which the data will be stored
        :return: 1 if success otherwise exception
        """
        return StudentSerializer.write(array, writer, filename)


class StudentSerializer:
    """Helper class for writing and reading from the stream"""
    __compatible_formats: list[str] = ['.json', '.csv']

    @staticmethod
    def read(reader, filename: str | None, data):
        """Method for reading from the stream

        :param reader: to read data from the file
        :param filename: the name of the file in which the data store
        :param data: to create an array of data not from a file
        :return: list of students
        """
        if filename is None and data is not None:
            return [
                Student(
                    firstname=row['first_name'],
                    lastname=row['last_name'],
                    year_of_birth=int(row['year_of_birth']),
                    year_of_enrollment=int(row['year_of_enrollment']),
                    idnp=int(row['idnp']),
                    faculty=row['faculty']
                ) for row in data
            ]
        # to use a file
        else:
            _, file_format = os.path.splitext(filename)
            if file_format in StudentSerializer.__compatible_formats:
                with open(filename, 'r', newline='') as file:
                    return [
                        Student(
                            firstname=row['first_name'],
                            lastname=row['last_name'],
                            year_of_birth=int(row['year_of_birth']),
                            year_of_enrollment=int(row['year_of_enrollment']),
                            idnp=int(row['idnp']),
                            faculty=row['faculty']
                        ) for row in reader(file)
                    ]
            raise Exception(f'{file_format} format is not compatible, use {StudentSerializer.__compatible_formats}')

    @staticmethod
    def write(array: list[Student], writer, filename: str | None):
        """Method for writing in  the stream

        :param writer: to write data in the file
        :param array: data which will be written
        :param filename: the name of the file in which the data will be stored
        :return: 1 if success otherwise exception
        """
        if filename is None:
            for student in array:
                print(student)
            return 1
        _, file_format = os.path.splitext(filename)
        if file_format in StudentSerializer.__compatible_formats:
            with open(filename, 'w', newline='') as file:
                match file_format.lower():
                    case '.csv':
                        fieldnames = [
                            'first_name',
                            'last_name',
                            'year_of_birth',
                            'year_of_enrollment',
                            'idnp',
                            'faculty'
                        ]
                        writer = writer(file, fieldnames=fieldnames)
                        writer.writeheader()
                        for student in array:
                            writer.writerow(StudentSerializer.prepare(student))
                    case '.json':
                        writer([StudentSerializer.prepare(student) for student in array], file)
                return 1

        raise Exception(f'{file_format} format is not compatible, use {StudentSerializer.__compatible_formats}')

    @staticmethod
    def prepare(obj: Student) -> dict:
        """Methods prepare data for writing in the file

        :param obj:
        :return: dict representation of student
        """
        return {
            "first_name": obj.firstname,
            "last_name": obj.lastname,
            "year_of_birth": obj.year_of_birth,
            "year_of_enrollment": obj.year_of_enrollment,
            "idnp": obj.idnp,
            "faculty": Faculty.get_faculty_name(obj.faculty)
        }
