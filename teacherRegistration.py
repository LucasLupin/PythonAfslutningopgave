from tec import TEC

subjects = []

def main_menu():
    print("\n\t\t""\033[31mM\033[0m""\033[33me\033[0m""\033[32mn\033[0m""\033[34mu\033[0m""\t\t")
    print("-------------------------------------")
    print("\t1. Create Teacher\t")
    print("\t2. Update Teacher\t")
    print("\t3. Show All Teachers\t")
    print("\t4. EXIT\t")

def main():
    tec = TEC()
    tec.load_teacher()
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            tec.create_teacher(tec)
        elif choice == '2':
            tec.update_teacher()
        elif choice == '3':
            tec.show_all_teachers()
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
