class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    @classmethod
    def count_instances(cls):
        print(f"total number of instances created with this class is {cls.count}")

    @classmethod
    def create_child(self, name, age=0):
        return self.create_child(name, age)

    def __str__(self):
        return f"{self.name} is {self.age}"
    
    def __repr__(self):
        return self.__str__()


Ebike = Person.create_child("Ebike", 28)
print(Ebike)
Person.count_instances()