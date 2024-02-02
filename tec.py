from teacher import Teacher

class TEC:
    def __init__(self):
        self.teachers = []
        self.subjects = []

    def create_teacher(self, tec):
        first_name = input("Enter teacher's first name: ")
        last_name = input("Enter teacher's last name: ")
        subject = tec.select_subject().strip().strip('"')

        new_teacher = Teacher(first_name, last_name, [subject])
        self.teachers.append(new_teacher)
        print(f"Teacher created: {new_teacher}")
        tec.save_teachers_to_file()
        return new_teacher

    def find_teacher(self, first_name, last_name):
        for teacher in self.teachers:
            if teacher.first_name == first_name and teacher.last_name == last_name:
                return teacher
        return None

    def show_all_teachers(self):
        if len(self.teachers) <= 0:
            print("\n\033[1;31mError:\033[0m There are no teachers in the list")
            print("-------------------------------------\n")
        else:
            print("\n\t\033[31mList\033[0m" " \033[33mOf\033[0m" " \033[32mTeacher´s\033[0m")
            print("-------------------------------------")
            print('\n\n'.join(str(teacher) for teacher in self.teachers))
    
    def select_subject(self,filename=r"C:\Users\lukr\Desktop\H3\Python\PythonAfslutningopgave\Subject.txt"):
        self.subjects.clear()
        with open(filename, "r") as file:
            for subject in file:
                # Strip end-of-line characters and outermost quotation marks
                clean_subject = subject.strip().strip('"')
                self.subjects.append(clean_subject)
        print("\nAvailable subjects:\n")
        for i, subject in enumerate(self.subjects, 1):
            # Subjects are now displayed without quotation marks
            print(f"[{i}] {subject}")
        while True:
            try:
                subject_number = int(input("\nChoose a subject from the list: "))
                if 1 <= subject_number <= len(self.subjects):
                    return self.subjects[subject_number - 1]  # Return the subject without quotation marks
                else:
                    print("Please select a valid number from the list.")
            except ValueError:
                print("Please enter a number.")
    
    def save_teachers_to_file(self, filename=r"C:\Users\lukr\Desktop\H3\Python\PythonAfslutningopgave\Teacher.txt"):
        with open(filename, "w") as file:
            for teacher in self.teachers:
                subjects_str = ', '.join(teacher.subjects).strip()
                line_to_save = f"{teacher.first_name} {teacher.last_name} {subjects_str}\n"
                file.write(line_to_save)
    
    def load_teacher(self, filename=r"C:\Users\lukr\Desktop\H3\Python\PythonAfslutningopgave\Teacher.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    cleaned_line = line.strip()
                    if cleaned_line:
                        parts = cleaned_line.split(' ', 2)
                        first_name, last_name = parts[0], parts[1]
                        # Assuming subjects are separated by ", " and removing possible quotation marks
                        subjects = [subject.strip().strip('"') for subject in parts[2].split(", ")]
                        self.teachers.append(Teacher(first_name, last_name, subjects))
        except FileNotFoundError:
            print("File not found. Starting with an empty list of teachers.")

    def update_teacher(tec):
        if len(tec.teachers) <=0:
            print("\n\033[1;31mError:\033[0m There are no teachers to update")
            print("-------------------------------------\n")
            return
        else:
            print("\n\tList of all teachers:")
            print("-------------------------------------\n")
            for i, teacher in enumerate(tec.teachers, 1):
                print(f"[{i}] {teacher}\n")
            try:
                teacher_number = int(input("Choose a teacher from the list: "))
                if not 1 <= teacher_number <= len(tec.teachers):
                    print("Please select a valid number from the list.")
                    return
            except ValueError:
                print("Please enter a number.")
                return
            
            # Get the selected teacher
            selected_teacher = tec.teachers[teacher_number - 1]
            print(f"\n\n{selected_teacher.first_name} is enrolled in the following subjects:")
            for subject in selected_teacher.subjects:
                print(f"- {subject}")
            print("\n[1] Add more subjects for the teacher.")
            print("[2] Remove a subject.")
            try:
                choice = int(input("Choose 1 or 2: \n"))
                if choice == 1:
                    new_subject = tec.select_subject()
                    print(new_subject)
                    selected_teacher.add_subject(new_subject)
                    print(f"Added {new_subject} to {selected_teacher.first_name}'s subjects.")
                    tec.save_teachers_to_file()
                elif choice == 2:
                    if not selected_teacher.subjects:
                        print(f"{selected_teacher.first_name} has no subjects to remove.")
                        return
                    for i, subject in enumerate(selected_teacher.subjects, 1):
                        print(f"[{i}] {subject}")
                    subject_number = int(input("Choose a subject to remove: "))
                    if 1 <= subject_number <= len(selected_teacher.subjects):
                        subject_to_remove = selected_teacher.subjects.pop(subject_number - 1)
                        print(f"Removed {subject_to_remove} from {selected_teacher.first_name}'s subjects.")
                        tec.save_teachers_to_file()
                    else:
                        print("Please select a valid subject number.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a number.")



