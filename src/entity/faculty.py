class Faculty:
    """Class representing the entity of the faculty"""
    faculties = [
        'Faculty of Biology and Geoscience',
        'Faculty of Chemistry and Chemical Technology',
        'Faculty of Law',
        'Faculty of Journalism and Communication Sciences',
        'Faculty of Physics and Engineering',
        'Faculty of History and Philosophy',
        'Faculty of Mathematics and Informatics',
        'Faculty of Philology',
        'Faculty of Economic Sciences',
        'Faculty of Psychology',
        'Faculty of International Relations'
    ]

    @staticmethod
    def get_faculty_name(index: int):
        """Returns string faculty name

        :param index: int representation of faculty
        :return: string representation of faculty
        """
        return Faculty.faculties[index]

    @staticmethod
    def get_faculty_index(name: str):
        """Returns string faculty index

        :param name: string representation of faculty
        :return: int representation of faculty
        """
        return Faculty.faculties.index(name)
