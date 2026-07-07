# EmpAdd.py ----> Module name
import pickle
def addEmployee():
    with open("CLI-PROJECT.data", "ab") as fp:
        print("_" * 50)
        empno = int(input("\tEnter employee number: "))
        empname = input("\tEnter employee name: ")
        empsal = float(input("\tEnter employee salary: "))
        print("_" * 50)
        # Create a iterable object and emp values
        lst = []
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        # Save list object to the file
        pickle.dump(lst, fp)
        print("\t\tEmployee details saved in file")
        print("_" * 50)