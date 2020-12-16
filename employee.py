# creation of class employee

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay


new_employee1 = Employee("raj", "kumar", 5000)

# the gives memory address location of employee1

print("The newly created employee :", new_employee1)
