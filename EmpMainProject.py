from EmpSearch import searchEmployee
from EmpUpdate import updateEmployee
while(True):
    try:
        Menu()
        ch = int(input("Enter your choice:"))

        match(ch):
            case 1:
                addEmployee()

            case 2:
                updateEmployee()

            case 3:
                deleteEmployee()

            case 4:
                viewsingleEmployee()

            case 5:
                viewAllEmployee()

            case 6:
                searchEmployee()

            case 7:
                print("\tThanks for using this project")
                sys.exit()

            case _:
                print("\t\tPlease try again. Invalid choice")

    except ValueError:
        print("Please don't enter alphabets or symbols.")