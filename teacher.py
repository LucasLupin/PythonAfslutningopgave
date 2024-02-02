from person import Person

class Teacher(Person):
    def __init__(self, first_name, last_name, subjects=None):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = subjects if subjects is not None else []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    def __str__(self):
        # Join subjects with a comma only if there are multiple subjects
        subjects_str = ", ".join(self.subjects)
        return f"{self.first_name} {self.last_name} Subjects: {subjects_str}"
