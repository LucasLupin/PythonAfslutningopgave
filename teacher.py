from person import Person

class Teacher(Person):
    def __init__(self, first_name, last_name, subjects=None):
        super().__init__(first_name, last_name)
        self.subjects = subjects if subjects is not None else []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    def __str__(self):
        return f"{super().__str__()}, Subjects: {', '.join(self.subjects)}"
