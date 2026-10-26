# Question 1: Student Marks Management System

## Problem Statement
Develop a simple Python program to manage student marks. The program should accept details of multiple students, calculate their results, and display a summary.

## Approach/Logic Used
1. Created helper functions for calculations (calculate_total, calculate_average, get_grade, get_result)
2. Used a loop to accept input for multiple students
3. Stored each student's data in a dictionary
4. Calculated total, average, grade, and result for each student
5. Displayed results in a formatted way

## How to Run the Program
```bash
python main.py
```

## Sample Input
How many students? 2

--- Student 1 ---
Student ID: 101
Student Name: Jisna
Python Marks: 100
SQL Marks: 100
AI Marks: 100

--- Student 2 ---
Student ID: 102
Student Name: Rahul
Python Marks: 85
SQL Marks: 80
AI Marks: 75


## Sample Output
===== Student Result =====
Student ID: 101
Name: Jisna
Total: 300
Average: 100.0
Grade: A+
Result: PASS

Student ID: 102
Name: Rahul
Total: 240
Average: 80.0
Grade: A
Result: PASS

## Python Concepts Used
1. Functions - Used helper functions for calculations
2. Lists & Dictionaries - Stored student data in dictionaries and list of dictionaries
3. Loops- Used for loop to iterate through multiple students
4. Conditional Statements - Used if-elif-else for grade assignment and PASS/FAIL
5. Input/Output- Used input() and print() for user interaction
6. Data Types- Used strings, integers, and floats