from teacher import Teacher

class TEC:
    def __init__(self):
        self.teachers = []

    def create_teacher(self, first_name, last_name, subject):
        new_teacher = Teacher(first_name, last_name, [subject])
        self.teachers.append(new_teacher)
        return new_teacher

    def find_teacher(self, first_name, last_name):
        for teacher in self.teachers:
            if teacher.first_name == first_name and teacher.last_name == last_name:
                return teacher
        return None

    def show_all_teachers(self):
        return '\n'.join(str(teacher) for teacher in self.teachers)
