class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print(self):
        print("name = "+ self.name+ " , age = " +str(self.age))    

Student = Student("romina",19)   
Student.print()