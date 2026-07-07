# EmpSearch.py ---> Module name
import pickle
def searchEmployee():
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
    for index in range(len(records)):
        if records[index][0] == empno:
            found = True
            break
    print("_" * 50)
    if found:
        print("\t\tEmployee Exists - Valid Employee")
    else:
        print("\t\tEmployee Does Not Exist")
    print("_" * 50)