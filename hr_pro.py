
employee_list = []
class Employee:
   #Employee class here
   def __init__(self, name, age, salary, employment_year):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_year = employment_year
   def get_working_years(self):
       return current_year - self.employment_year


manager_list = []
class Manager(Employee):
    #Manager class here
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage
    def get_bonus(self):
        return float(self.bonus_percentage) * float(self.salary)






def main():
    # main code here
    print ("Welcome to HR Pro 2019")
    print ("""
    Options:
        1. Show Show Employees
        2. Show Managers
        3. Add An Employee
        4. Add A Manager
        5. Exit
        """)
    choose = int(input("What would you like to do? "))
    print("------------------")
    while choose != 5:
        if choose == 1:
            for employee_info in employee_list:
                print(f"Name: {employee_info.name}, Age: {employee_info.age}, Salary: {employee_info.salary}, Working years: {employee_info.get_working_years}")
        elif choose == 2:
            for mngr in manager_list:
                print(f"Name: {mngr.name}, Age: {mngr.age}, Salary: {mngr.salary}, Working years: {mngr.get_working_years}, Bonus: {mngr.get_bonus}")
        elif choose == 3:
            name_inp = input("Name:  ")
            age_inp = input("Age:  ")
            salary_inp = float(input("Salary:  "))
            employment_year_inp = int(input("Employment year:  "))
            employee_list.append(Employee(name_inp,age_inp,salary_inp,employment_year_inp))
            print("Employee added succesfully")

        elif choose == 4:
            name_inp = input("Name:  ")
            age_inp = input("Age:  ")
            salary_inp = float(input("Salary:  "))
            employment_year_inp = int(input("Employment year:  "))
            bonus_inp = float(input("Bonus Percentage:  "))
            manager_list.append(Manager(name_inp,age_inp,salary_inp,employment_year_inp,bonus_inp))
            print("Manager added succesfully")
        else:
            break

        print("Welcome to HR Pro 2019")
        print ("""
        Options:
            1. Show Show Employees
            2. Show Managers
            3. Add An Employee
            4. Add A Manager
            5. Exit
            """)
        choose = int(input("What would you like to do? "))









if __name__ == '__main__':
    main()
