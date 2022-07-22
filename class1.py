class Student:
    def __init__(self, name, age, GPA):
        self.name = name
        #the left name and the right name is not the same
        self.age = age
        self.GPA = GPA
        
    def myfunc(self):
        print("hello my name is" ,self.name, "my age is " , self.age, "my GPA is ?" , self.GPA)

p1 = Student("john", 36, 3.3)
p1.myfunc()

class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def myfunc1(self):
        print("hello the course name is" ,self.name, "the course duration in days is " , self.duration)

p1 = Course("AI", 30)
p1.myfunc1()
