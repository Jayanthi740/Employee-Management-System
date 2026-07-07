# EmpView.py ---> Module name
import pickle
def viewsingleEmployee():
    records = []
    with open("CLI-PROJECT.data", "rb") as fp:
        while True:
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    found = False
    empno = int(input("Enter employee number: "))
    for record in records:
        if record[0] == empno:
            found = True
            break
    print("_" * 50)
    if found:
        print("Employee Number : {}".format(record[0]))
        print("Employee Name   : {}".format(record[1]))
        print("Employee Salary : {}".format(record[2]))
    else:
        print("Record does not exist")
    print("_" * 50)
def viewAllEmployee():
    with open("CLI-PROJECT.data", "rb") as fp:
        print("_" * 50)
        print("\tEno\tName\tSalary")
        print("_" * 50)
        while True:
            try:
                record = pickle.load(fp)
                print("\t{}\t{}\t{}".format(record[0], record[1], record[2]))
            except EOFError:
                print("_" * 50)
                break