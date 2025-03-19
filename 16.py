a=input("Enter the name of student : ")
b=input("Enter the age of student : ")
c=input("Enter the course : ")

class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def diplay_info(self):
        print(f'name : {self.name}\nage : {self.age}\ncourse : {self.course}')

p1=student(a, b ,c)
p1.diplay_info()