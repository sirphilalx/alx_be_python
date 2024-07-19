class Student:
    def __init__(self, first_name=None, last_name=None, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_name(self):
        print(f'{self.first_name} {self.last_name}') 
    
    def student_description(self):
        print(f'{self.first_name} {self.last_name} is {self.age} years old')

Joel = Student('Joel', 'Ugbebor', 13)
Joel.display_name()
Joel.student_description()