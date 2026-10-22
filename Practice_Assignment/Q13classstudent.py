class Student :
    def __init__(self,name,rollnumber,mark):
        self.name=name
        self.rollnumber=rollnumber
        self.mark=mark

    def display_details(self):
        print("The name of student is ",self.name)
        print("The rollnumber of student is ",self.rollnumber)
        print("The mark of student is ",self.mark)
    def check_results(self):
        if(self.mark>=40):
            return "Pass"
        else:
            return "Fail"
student1=Student("Jisna",13,99)
student2=Student("Nabeel",21,91)
student3=Student("Dilawar",13,100)
print("=== Student 1 ===")
student1.display_details()
print("Result:", student1.check_results())

print("\n=== Student 2 ===")
student2.display_details()
print("Result:", student2.check_results())

print("\n=== Student 3 ===")
student3.display_details()
print("Result:", student3.check_results())

