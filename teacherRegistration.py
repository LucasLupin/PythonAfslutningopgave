from tec import TEC
from teacher import Teacher

tec = TEC()
subjects = []

def main_menu():
    print("\n\t\t""\033[31mM\033[0m""\033[33me\033[0m""\033[32mn\033[0m""\033[34mu\033[0m""\t\t")
    print("-------------------------------------")
    print("\t1. Create Teacher\t")
    print("\t2. Update Teacher\t")
    print("\t3. Show All Teachers\t")
    print("\t4. EXIT\t")

def load_teacher(filename=r"C:\Users\lukr\Desktop\H3\Python\PythonAfslutningopgave\Teacher.txt"):
    global tec
    with open(filename, "r") as file:
        for line in file:
            print(f"Read line: {line}")  # Debugging print
            if line.strip() and '"' in line:
                parts = line.strip().split(' ', 2)
                first_name, last_name = parts[0], parts[1]
                subjects_str = parts[2].strip().strip('"')
                subjects = subjects_str.split(',') if subjects_str else []
                print(f"Adding teacher: {first_name} {last_name} with subjects {subjects}")  # Debugging print
                tec.teachers.append(Teacher(first_name, last_name, subjects))
            else:
                print(f"Skipping invalid or empty line: {line}")  # Debugging print
    return tec

def select_subject(filename=r"C:\Users\lukr\Desktop\H3\Python\PythonAfslutningopgave\Subject.txt"):
    subjects.clear()
    with open(filename, "r") as file:
        for subject in file:
            subjects.append(subject)
    print("Available subjects:")
    for i, subject in enumerate(subjects, 1):
        # Use end parameter to control what is printed after each subject.
        print(f"[{i}] {subject}", end='' if i < len(subjects) else '\n')
    while True:
        try:
            subject_number = int(input("\nChoose a subject from the list: "))
            if 1 <= subject_number <= len(subjects):
                return subjects[subject_number - 1]
            else:
                print("Please select a valid number from the list.")
        except ValueError:
            print("Please enter a number.")

def update_teacher(tec):
    if len(tec.teachers) <=0:
        print("\n\033[1;31mError:\033[0m There are no teachers to update")
        print("-------------------------------------\n")
        return
    else:
        print("List of all teachers:")
        for i, teacher in enumerate(tec.teachers, 1):
            print(f"[{i}] {teacher}")
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
        print(f"{selected_teacher.first_name} is enrolled in the following subjects:")
        for subject in selected_teacher.subjects:
            print(f"- {subject}")
        print("[1] Add more subjects for the teacher.")
        print("[2] Remove a subject.")
        try:
            choice = int(input("Choose 1 or 2: "))
            if choice == 1:
                new_subject = select_subject()
                selected_teacher.add_subject(new_subject)
                print(f"Added {new_subject} to {selected_teacher.first_name}'s subjects.")
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
                else:
                    print("Please select a valid subject number.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")


def create_teacher(tec):
    first_name = input("Enter teacher's first name: ")
    last_name = input("Enter teacher's last name: ")
    subject = select_subject().strip()  # Strip leading/trailing whitespace from the selected subject

    # Create the teacher and add to the tec object
    teacher = tec.create_teacher(first_name, last_name, subject)
    print(f"Teacher created: {teacher}")

    with open(r"C:\Users\lukr\Desktop\H3\Python\PythonAfslutningopgave\Teacher.txt", "a") as file:
        subject_str = subject if isinstance(subject, str) else ','.join(subject)
        file.write(f"{first_name} {last_name} \"{subject_str}\"\n")


def show_all_teachers(tec):
    if len(tec.teachers) <=0:
        print("\n\033[1;31mError:\033[0m There are no teachers in the list")
        print("-------------------------------------\n")

        return
    else:
        print(tec.show_all_teachers())

def main():
    global tec
    tec = load_teacher()
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            create_teacher(tec)
        elif choice == '2':
            update_teacher(tec)
        elif choice == '3':
            show_all_teachers(tec)
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
