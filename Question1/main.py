def calculate_total(python_marks,sql_marks,ai_marks):
    total=python_marks+sql_marks+ai_marks
    return total
def calculate_average(total):
    average=total/3
    return average
def get_grade(average):
   
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
def get_result(average):
    
    if average >= 40:
        return "PASS"
    else:
        return "FAIL"

def display_student(student):
  
    print("Student ID:", student["id"])
    print("Name:", student["name"])
    print("Total:", student["total"])
    print("Average:", student["average"])
    print("Grade:", student["grade"])
    print("Result:", student["result"])
num_students = int(input("How many students? "))
students = []

for i in range(num_students):
    print("\n--- Student", i+1, "---")
    
    # Get input for ONE student
    student_id = input("Student ID: ")
    student_name = input("Student Name: ")
    python_marks = int(input("Python Marks: "))
    sql_marks = int(input("SQL Marks: "))
    ai_marks = int(input("AI Marks: "))
    
    student = {
        "id": student_id,
        "name": student_name,
        "python": python_marks,
        "sql": sql_marks,
        "ai": ai_marks
    }
    student["total"]=calculate_total(python_marks,sql_marks,ai_marks)
    student["average"]=calculate_average(student["total"])
    student["grade"]=get_grade(student["average"])
    student["result"]=get_result(student["average"])
    students.append(student)

print("All students saved!")

print("===== Student Result =====")
for student in students :
    display_student(student)
    print()
