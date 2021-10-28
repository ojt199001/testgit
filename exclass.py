class Student:
    def printInfo(self):
        print(f"full name: {self.name}")
st1 = Student()
st1.name = ("O J T")
st1.printInfo()
del st1.name
del st1
print("---------------------")
class Dog:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    def say(self):
        print(f"GOGO, my name is {self.name}")
mydog = Dog()
mydog.say()
mydog.name = "OJT"
mydog.say()
print("-------------------------")
class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    def old(self):
        return 2022 - self.year
mycar = Car(2021, "Mazda", "Mazda 2 - Sport")
print("My car is {} years old".format(mycar.old()))
print("--------------------------------")
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    # def printage(self):
    #     print(self.age)
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    def printage(self):
        print(self.age)
st = Student("Hoàng", "Nam", 19)
st.printname()
# st.age = 20
st.printage()

print("---------------------------")