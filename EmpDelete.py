# EmpDelete.py ----> Module name
import pickle
def deleteEmployee():
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
            recindex = index
            found = True
            break
    print("_" * 50)
    if found:
        del records[recindex]
        with open("CLI-PROJECT.data", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("\t\tEmployee record deleted - verify")
    else:
        print("\t\tEmployee record NOT found")
    print("_" * 50)