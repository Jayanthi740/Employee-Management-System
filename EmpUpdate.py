# EmpUpdate.py
import pickle
def updateEmployee():
    records = []
    with open("CLI-PROJECT.data", "rb") as fp:
        while True:
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                print("_" * 50)
                break
    found = False
    empno = int(input("Enter employee number:"))
    for index in range(len(records)):
        if records[index][0] == empno:
            recindex = index
            found = True
            break
    print("_" * 50)
    if found:
        newsal = float(input("Enter the new salary:"))
        records[recindex][2] = newsal
        # Re-write the modified record to the file
        with open("CLI-PROJECT.data", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("Employee salary updated--verify")
    else:
        print("\t\tEmployee number does not exist")
    print("_" * 50)