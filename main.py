import sys
from EmployeeClass import *
#Dictionary that provides the menu
EmployeeDict = {
    "1":"Add Employee",
    "2":"View Employee Credentials (by full Name)",
    "3":"Edit Employee Credentials",
    "4":"Employee Promotion",
    "5":"Delete Employee",
    "6":"Search Employee (by ID)",
    "7":"Exit"

}
#The "ghost" variable run is the switch keep the program open or closed ( closed when the value equals 0 or the admin uses an exit function)
run = 1
while run !=0:
    #Menu intro browse
    print("Welcome to the Employee Management Dashboard! \n MENU")
    for i in EmployeeDict:
        print(i,":",EmployeeDict[i])
    #variable that the user inputs to browse in the menu
    choice = str(input( "Please choose the menu option you would like to access by typing the number that corresponds to the option! \n"))
    #Type Check
    while choice <"1" and choice>"7":
        choice = str(input("Please select a valid menu option! \n"))
    #choice check and menu functions imported by the class

    #1 : Add Employee
    if choice =="1":
        print("Welcome to the" , EmployeeDict[choice], "menu." )
        add_employee = EmployeeClass()
        add_employee.add_employee()

    #2 : View Employee Credentials
    elif choice == "2":
        print("Welcome to the", EmployeeDict[choice], "menu.")
        view_emp = EmployeeClass()
        view_emp.view_emp()

    #3 : Edit Employee Credentials
    elif choice == "3":
        print("Welcome to the", EmployeeDict[choice], "menu.")
        edit_emp = EmployeeClass()
        edit_emp.edit_emp()

    #4 : Employee Promotion
    elif choice == "4":
        print("Welcome to the", EmployeeDict[choice], "menu.")
        prom_emp = EmployeeClass()
        prom_emp.prom_emp()

    #5 : Delete Employee
    elif choice == "5":
        print("Welcome to the", EmployeeDict[choice], "menu.")
        del_emp = EmployeeClass()
        del_emp.del_emp()

    #6 : Search Employee
    elif choice == "6":
        print("Welcome to the", EmployeeDict[choice], "menu.")
        src_emp = EmployeeClass()
        src_emp.src_emp()

    #7: Exit
    elif choice == "7":
        e= str(input("Are you sure you want to Exit? \n YES(y) or NO(n)"))
        while e!="y" and e!="n":
            e=str(input("Please choose between YES(y) or NO(n)"))
        if e=="y":
            sys.exit("Employee Management Dashboard is closing!")
        else:
            continue



