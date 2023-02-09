#Connector import
import mysql.connector as mysql
#Database import
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "employee_database"
)
#Our cursor
db_cursor =db.cursor()
#Class that uses its objects to create menu functions plus the starting values of the table
class EmployeeClass:
    def __init__(self):
        self.EmpId = 0
        self.EmpName = ""             #Set not to be null in database
        self.EmpSurname = ""          #Set not to be null in database
        self.Email = ""
        self.ContactPh= 0
        self.Address = ""
        self.Payroll = 0

#1 : Add Employee function
    def add_employee(self):
        #Ghost variable to switch on the loop (for the checker in the end and the repetition of the function)
        ret=1
        while ret!=0:
            #Credentials added by user
            EmpName = str(input("Please fill in the name of the new Employee "))
            #Checker if value is null or numeric
            while not(EmpName) or EmpName.isnumeric():
                EmpName = str(input("The name of the new Employee MUST be filled in (and) with characters!"))
            EmpSurname = str(input("Please fill in the surname of the new Employee "))
            # Checker if value is null
            while not(EmpSurname) or EmpSurname.isnumeric():
                EmpSurname = str(input("The surname of the new Employee MUST be filled in (and) with characters!"))
            Email = str(input("Please fill in the email of the new Employee "))
            ContactPh = str(input("Please fill in the contact phone of the new Employee "))
            #Checker if phone is numeric and 10 digits
            while not(ContactPh.isnumeric()) or len(ContactPh)<10:
                ContactPh = str(input("Please fill in the contact phone of the new Employee with the proper credentials "))
            Address = str(input("Please fill in the address of the new Employee "))
            Payroll =str(input("Please fill in the payroll of the new Employee "))
            while Payroll.isalpha():
                Payroll = str(input("Please fill in the payroll of the new Employee with numbers!"))
            #Addition query
            addition =[EmpName,EmpSurname,Email,ContactPh,Address,Payroll]
            addemp_query = "INSERT INTO `hr` (`EmpName`, `EmpSurname`, `Email`, `ContactPh`, `Address`, `Payroll`) VALUES (%s, %s, %s, %s, %s, %s)"
            db_cursor.execute(addemp_query,addition)
            db.commit()
            print(db_cursor.rowcount, "Added successfully to the database! ")
            #Return to main menu checker
            sure = input("Do you want to return to the Main Menu or you want to add another employee? \n RETURN(r) or STAY(s)")
            while sure != "r" and sure != "s":
                sure = str(input("Please choose between RETURN(r) or STAY(s)"))
            if sure == "r":
                break
            else:
                continue

#2 : View Employee Credentials function
    def view_emp(self):
        #Ghost variable to switch on the loop (for the checker in the end and the repetition of the function)
        ret=1
        while ret!=0:
            EmpName = str(input("Please fill in the name of the  Employee "))
            # Checker if value is null or numeric
            while not(EmpName) or EmpName.isnumeric():
                EmpName = str(input("The name of the  Employee MUST be filled in (and) with characters!"))
            EmpSurname = str(input("Please fill in the surname of the  Employee "))
            # Checker if value is null or numeric
            while not (EmpSurname) or EmpSurname.isnumeric():
                EmpSurname = str(input("The surname of the  Employee MUST be filled in (and) with characters!"))
            #View person via Full Name query
            searchPerson = [EmpName,EmpSurname]
            viewemp_query = "SELECT * FROM`hr`WHERE EmpName =(%s) AND EmpSurname = (%s) "
            db_cursor.execute(viewemp_query,searchPerson)
            result = db_cursor.fetchall()
            if not(result):
                print("No Employee Found")
            else:
                print(result , "Employee found! ")
            sure = input("Do you want to return to the Main Menu or to search for another employee? \n RETURN(r) or STAY(s)")
            # Return to main menu checker
            while sure not in "RrSs":
                sure = str(input("Please choose between RETURN(r) or STAY(s)"))
            if sure in "Rr":
                break
            else:
                continue

#3 : Edit Employee Credentials function
    def edit_emp(self):
        # Ghost variable to switch on the loop (for the checker in the end and the repetition of the function)
        ret=1
        while ret!=0:
            # Checker for the type of search (via ID or Full Name )
            src = str(input("Do you want to search for the employee via ID(1) or Full Name(2) "))
            while src != "1" and src != "2":
                src = str(input("Please choose between ID(1) or Full Name(2)"))
            #Option ID search
            if src=="1":
                EmpId = str(input("Please fill in the ID of the  Employee you are trying to find"))
                #Checker if id is null or not numeric
                while not (EmpId.isnumeric()):
                    EmpId = str(input("Please give an Id 'NUMBER' "))
                else:
                    id = (EmpId,)
                #Id search query
                srcemp_query = "SELECT * FROM`hr`WHERE EmpId =(%s) "
                db_cursor.execute(srcemp_query, id)
                result = db_cursor.fetchone()
                print(result)
                #Checker if there is no result
                if not(result):
                    print("No entry found")
                    sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
                    while sure != "y" and sure != "n":
                        sure = str(input("Please choose between YES(y) or NO(n)"))
                    if sure == "y":
                        break
                    else:
                        continue
            # Option Full Name search
            else:
                EmpName = str(input("Please fill in the name of the  Employee "))
                # Checker if value is null or numeric
                while not (EmpName) or EmpName.isnumeric():
                    EmpName = str(input("The name of the  Employee MUST be filled in (and) with characters!"))
                EmpSurname = str(input("Please fill in the surname of the  Employee "))
                # Checker if value is null or numeric
                while not (EmpSurname) or EmpSurname.isnumeric():
                    EmpSurname = str(input("The surname of the  Employee MUST be filled in (and) with characters!"))
                #Search person query
                searchPerson = [EmpName, EmpSurname]
                viewemp_query = "SELECT * FROM`hr`WHERE EmpName =(%s) AND EmpSurname = (%s) "
                db_cursor.execute(viewemp_query, searchPerson)
                result = db_cursor.fetchall()
                print(result)
                # Checker if there is no result
                if not(result):
                    print("No entry found")
                    sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
                    while sure != "y" and sure != "n":
                        sure = str(input("Please choose between YES(y) or NO(n)"))
                    if sure == "y":
                        break
                    else:
                        continue
            #casting result as a list to be able to configure its contents
            result=list(result)
            #Ghost Variable to switch on the loop ( for the checker in the end and the repetition of the function)
            conf=1
            while conf!=0:
                i=str(input("Please select which details you want to configure by pressing the proper number \n 1: Name \n 2: Surname \n 3: Email \n 4: Contact Phone \n 5: Adress \n"))
                #Checker for right value
                while i<"0" and i>"6":
                    i = str(input("Please select from the numbers as shown \n 1: Name \n 2: Surname \n 3: Email \n 4: Address \n 5: Adress \n"))
                else:
                    i=int(i) #for some reason I had an error so I cast it as an int
                    result[i]=input("Please insert the correct credential")
                    #Checker for name and surname (cannot be blank)
                    while (i==1 or i==2) and (not(result[i]) or result[i].isnumeric()):
                        result[i] = input("Credential cannot be blank or numeric.Please insert the correct credential")
                    #Checker if user is finished editing or wants to edit another credential
                    stop = str(input("Have you finished the configurations \n YES(y) or NO(n)"))
                    while stop != "y" and stop != "n":
                        stop = str(input("Please choose between YES(y) or NO(n)"))
                if stop == "y":
                    break
                else:
                    continue
            #Edit credentials query
            editemp_query = "UPDATE `hr` SET `EmpName`=(%s),`EmpSurname`=(%s),`Email`=(%s),`ContactPh`=(%s),`Address`=(%s)"
            result2=(result[1],result[2],result[3],result[4],result[5])
            db_cursor.execute(editemp_query, result2)
            db.commit()
            print(result2,"\n Configuration Successful ")
            #Return to main menu checker
            sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
            while sure != "y" and sure != "n":
                sure = str(input("Please choose between YES(y) or NO(n)"))
            if sure == "y":
                print("Returning to the Main Menu")
                break
            else:
                continue

#4 : Employee Promotion function
    def prom_emp(self):
        # Ghost variable to switch on the loop (for the checker in the end and the repetition of the function)
        ret=1
        while ret!=0:
            #Search type checker
            src = str(input("Do you want to search for the employee via ID(1) or Full Name(2) "))
            while src != "1" and src != "2":
                src = str(input("Please choose between ID(1) or Full Name(2)"))
            #Option ID
            if src=="1":
                EmpId = str(input("Please fill in the ID of the  Employee you are trying to find"))
                #Value checker ( if null or not numeric)
                while not (EmpId.isnumeric()):
                    EmpId = str(input("Please give an Id 'NUMBER' "))
                else:
                    id = (EmpId,)
                #search query
                srcemp_query = "SELECT * FROM`hr`WHERE EmpId =(%s) "
                db_cursor.execute(srcemp_query, id)
                result = db_cursor.fetchone()
                print(result)
                #Checker if entry is not found
                if not(result):
                    print("No entry found")
                    #return checker
                    sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
                    while sure != "y" and sure != "n":
                        sure = str(input("Please choose between YES(y) or NO(n)"))
                    if sure == "y":
                        break
                    else:
                        continue
            #Option Full Name
            else:
                EmpName = str(input("Please fill in the name of the  Employee to be promoted "))
                # Checker if value is null or numeric
                while not (EmpName) or EmpName.isnumeric():
                    EmpName = str(input("The name of the  Employee MUST be filled in (and) with characters!"))
                EmpSurname = str(input("Please fill in the surname of the  Employee to be promoted"))
                # Checker if value is null or numeric
                while not (EmpSurname) or EmpSurname.isnumeric():
                    EmpSurname = str(input("The surname of the  Employee MUST be filled in (and) with characters!"))
                #search person query
                searchPerson = [EmpName, EmpSurname]
                viewemp_query = "SELECT * FROM`hr`WHERE EmpName =(%s) AND EmpSurname = (%s) "
                db_cursor.execute(viewemp_query, searchPerson)
                result = db_cursor.fetchall()
                print(result)
                # Result not found checker
                if not(result):
                    print("No entry found")
                    sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
                    while sure != "y" and sure != "n":
                        sure = str(input("Please choose between YES(y) or NO(n)"))
                    if sure == "y":
                        break
                    else:
                        continue
            #result cast as list to be able to edit its contents
            result = list(result)
            result[6]=str(input("Please edit the Payroll of the employee that has been promoted! "))

            #blank payroll value checker
            while not(result[6]) or result[6].isalpha() :#I wanted to check if it is also a number but couldnt find the way
                result[6] = str(input("The Payroll of the Employee MUST be filled in (and) with numbers to continue!"))
            #promotion query
            promemp_query = "UPDATE `hr` SET `Payroll`=(%s) "
            result2 = (result[6],)
            db_cursor.execute(promemp_query, result2)
            db.commit()
            print("\n Promotion Successful, Payroll changed to ",result2)
            #return to main menu checker
            sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
            while sure != "y" and sure != "n":
                sure = str(input("Please choose between YES(y) or NO(n)"))
            if sure == "y":
                break
            else:
                continue

#5 : Delete Employee function
    def del_emp(self):
        # Ghost variable to switch on the loop (for the checker in the end and the repetition of the function)
        check=1
        while check!=0:
            #search type checker
            src = str(input("Do you want to search for the employee via ID(1) or Full Name(2) "))
            while src != "1" and src != "2":
                src = str(input("Please choose between ID(1) or Full Name(2)"))
            #Option ID
            if src=="1":
                EmpId = str(input("Please fill in the ID of the  Employee you are trying to find"))
                #checker if id is null or not numeric
                while not (EmpId.isnumeric()):
                    EmpId = str(input("Please give an Id 'NUMBER' "))
                else:
                    id = (EmpId,)
                #search by id query
                srcemp_query = "SELECT * FROM`hr`WHERE EmpId =(%s) "
                db_cursor.execute(srcemp_query, id)
                result = db_cursor.fetchone()
                print(result)
                #no entry found checker
                if not(result):
                    print("No entry found")
                    sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
                    while sure != "y" and sure != "n":
                        sure = str(input("Please choose between YES(y) or NO(n)"))
                    if sure == "y":
                        break
                    else:
                        continue
                #Checker if user wants to delete entry
                sure = input(" Are you sure you want to delete this employee entry? \n YES(y) or NO(n)")
                while sure != "y" and sure != "n":
                    sure = str(input("Please choose between YES(y) or NO(n)"))
                if sure == "y":
                    # delete entry query
                    delemp_query = "DELETE FROM `hr` WHERE EmpId =(%s) "
                    db_cursor.execute(delemp_query, id)
                    db.commit()
                    print("Entry/ies deleted successfuly! ")
            #Option Full Name
            else:
                EmpName = str(input("Please fill in the name of the  Employee entry you want to delete"))
                # Checker if value is null or numeric
                while not (EmpName) or EmpName.isnumeric():
                    EmpName = str(input("The name of the new Employee MUST be filled in (and) with characters!"))
                EmpSurname = str(input("Please fill in the surname of the  Employee "))
                # Checker if value is null or numeric
                while not (EmpSurname) or EmpSurname.isnumeric():
                    EmpSurname = str(input("The surname of the new Employee MUST be filled in (and) with characters!"))
                #search person query
                searchPerson = [EmpName, EmpSurname]
                viewemp_query = "SELECT * FROM`hr`WHERE EmpName =(%s) AND EmpSurname = (%s) "
                db_cursor.execute(viewemp_query, searchPerson)
                result = db_cursor.fetchall()
                print(result)
                #no entry found checker
                if not (result):
                    print("No entry found")
                    sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
                    while sure != "y" and sure != "n":
                        sure = str(input("Please choose between YES(y) or NO(n)"))
                    if sure == "y":
                        break
                    else:
                        continue
                #Checker if user wants to delete entry
                sure = input(" Are you sure you want to delete this employee entry? \n YES(y) or NO(n)")
                while sure != "y" and sure != "n":
                    sure = str(input("Please choose between YES(y) or NO(n)"))
                if sure == "y":
                    #delete entry query
                    delemp_query= "DELETE FROM `hr` WHERE EmpName =(%s) AND EmpSurname = (%s)"
                    db_cursor.execute(delemp_query, searchPerson)
                    db.commit()
                    print("Entry/ies deleted successfuly! ")

            #checker if user has finished deleting entries
            sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
            while sure != "y" and sure != "n":
                sure = str(input("Please choose between YES(y) or NO(n)"))
            if sure == "y":
                break
            else:
                continue

#6 : Search Employee function
    def src_emp(self):
        # Ghost variable to switch on the loop (for the checker in the end and the repetition of the function)
        ret=1
        while ret!=0:
            EmpId = str(input("Please fill in the ID of the  Employee you are trying to find"))
            # checker if id is null or not numeric
            while not(EmpId.isnumeric()) :
                EmpId = str(input("Please give an Id 'NUMBER' "))
            else:
                id=(EmpId,)
            #search by id query
            srcemp_query = "SELECT * FROM`hr`WHERE EmpId =(%s) "
            db_cursor.execute(srcemp_query, id)
            result = db_cursor.fetchone()
            print(result, "Employee found! \n Returning to the Main Menu")
            sure = input("Do you want to return to the Main Menu? \n YES(y) or NO(n)")
            while sure != "y" and sure != "n":
                sure = str(input("Please choose between YES(y) or NO(n)"))
            if sure == "y":
                break
            else:
                continue