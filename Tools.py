#Template for Car with its attributes
class Car:
    def __init__(self,color,size,model,person=''):
        self.color=color
        self.size= size
        self.model = model
        self.person = person

#Template for Student with attributes 
class Student:
    def __init__(self,name, major, gpa,probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.probation = probation
