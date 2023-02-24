class Student:
    def __init__(
            self,
            firstname: str = 'empty',
            lastname: str = 'empty',
            faculty: str = 'empty',
            year_of_birth: int = 0000,
            year_of_enrollment: int = 0000,
            idnp: int = 0000000000000
    ):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__idnp = idnp
        self.__year_of_enrollment = year_of_enrollment
        self.__year_of_birth = year_of_birth
        self.__faculty = faculty

    def __copy__(self):
        copy_instance = Student(
            firstname=self.firstname,
            lastname=self.lastname,
            idnp=self.idnp,
            year_of_enrollment=self.year_of_enrollment,
            year_of_birth=self.year_of_birth,
            faculty=self.faculty
        )
        return copy_instance

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        self.__faculty = value

    @property
    def year_of_birth(self):
        return self.__year_of_birth

    @year_of_birth.setter
    def year_of_birth(self, value):
        self.__year_of_birth = value

    @property
    def year_of_enrollment(self):
        return self.__year_of_enrollment

    @year_of_enrollment.setter
    def year_of_enrollment(self, value):
        self.__year_of_enrollment = value

    @property
    def idnp(self):
        return self.__idnp

    @idnp.setter
    def idnp(self, value):
        self.__idnp = value

    def assign(self, other):
        self.firstname = other.firstname
        self.lastname = other.lastname
        self.faculty = other.faculty
        self.year_of_birth = other.year_of_birth
        self.year_of_enrollment = other.year_of_enrollment
        self.idnp = other.idnp

    def __str__(self):
        return f'firstname:{self.firstname}, ' \
               f'lastname: {self.lastname}, ' \
               f'faculty: {self.faculty}, ' \
               f'year of birth: {self.year_of_birth}, ' \
               f'year of enrollment: {self.__year_of_enrollment}, ' \
               f'idnp: {self.idnp}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.firstname == other.firstname and \
                self.lastname == other.lastname and \
                self.faculty == other.faculty and \
                self.year_of_birth == other.year_of_birth and \
                self.year_of_enrollment == other.year_of_enrollment and \
                self.idnp == other.idnp
        return False

    @staticmethod
    def reading_from_stream(filename: str, reader):
        with open(filename, 'r', newline='') as csvfile:
            data = reader(csvfile)
            for row in data:
                yield Student(
                    firstname=row['first_name'],
                    lastname=row['last_name'],
                    year_of_birth=int(row['year_of_birth']),
                    year_of_enrollment=int(row['year_of_enrollment']),
                    idnp=int(row['idnp']),
                    faculty=row['faculty']
                )

    @staticmethod
    def writing_in_stream(obj, filename: str, writer):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['first_name', 'last_name', 'year_of_birth', 'year_of_enrollment', 'idnp', 'faculty']
            writer = writer(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({
                'first_name': obj.firstname,
                'last_name': obj.lastname,
                'year_of_birth': obj.year_of_birth,
                'year_of_enrollment': obj.year_of_enrollment,
                'idnp': obj.idnp,
                'faculty': obj.faculty
            })
