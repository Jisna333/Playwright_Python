class Employee:

    
    def __init__(self, employee_id, name, role, salary):
       
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary
    
    def display_details(self):
       
        return self.employee_id + " - " + self.name + " - " + self.role + " - ₹" + str(self.salary)
def read_employees(filename):
    
    employees = []
    
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  
            
            if line:  
              
                data = line.split(',')
                emp = Employee(data[0], data[1], data[2], int(data[3]))
                employees.append(emp)
    
    return employees
def find_highest_salary(employees):
   
    highest_employee = employees[0]
    
    for emp in employees:
        if emp.salary > highest_employee.salary:
            highest_employee = emp
    
    return highest_employee
def count_by_role(employees):
    
    role_count = {}
    
    for emp in employees:
        if emp.role in role_count:
            role_count[emp.role] = role_count[emp.role] + 1
        else:
            role_count[emp.role] = 1
    
    return role_count

filename = "employees.txt"

employees = read_employees(filename)


print("===== Employee Details =====\n")
for emp in employees:
    print(emp.display_details())

print("\n")

print("===== Employees with Salary > 50000 =====\n")
for emp in employees:
    if emp.salary > 50000:
        print(emp.display_details())

print("\n")

print("===== Highest Paid Employee =====\n")
highest = find_highest_salary(employees)
print(highest.display_details())

print("\n")

print("===== Employee Count by Role =====\n")
role_count = count_by_role(employees)
for role, count in role_count.items():
    print(role, ":", count)