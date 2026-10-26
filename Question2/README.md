# Question 2: Employee File Management System

## Problem Statement
Develop a Python application to manage employee information. Employee details are stored in a file and read to generate reports on salaries and roles.

## Approach/Logic Used
1. Created an Employee CLASS with attributes (employee_id, name, role, salary)
2. Created display_details() method to show employee information
3. Used read_employees() function to read from file using context manager
4. Implemented find_highest_salary() function to find highest paid employee
5. Created count_by_role() function to count employees by their roles
6. Used context manager (with open()) for safe file handling

## How to Run the Program

cd Question2
python main.py

## Sample Input (employees.txt)
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
## Sample Output

===== Employee Details =====

101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000

===== Employees with Salary > 50000 =====

103 - John - Developer - ₹60000

===== Highest Paid Employee =====

103 - John - Developer - ₹60000

===== Employee Count by Role =====

Python Developer : 1
Tester : 2
Developer : 1


## Python Concepts Used
1. Object-Oriented Programming (OOP) - Created Employee class with constructor and methods
2. File Handling - Read data from employees.txt file
3. Context Manager- Used `with open()` for safe file handling
4. Functions - Created functions for different operations
5. Loops - Used for loops to iterate through employees
6. Conditional Statements - Used if conditions to filter and compare
7. Dictionaries - Used to store role counts
8. String Methods - Used split(), strip() for data processing