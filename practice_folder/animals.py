class Animal:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def __str__(self):
        print(f"the name of this animal is {self.name} and he eats {self.eat} and {self.sleep} too")


    def __repr__(self):
        return self.__str__()