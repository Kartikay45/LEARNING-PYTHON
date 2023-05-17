#OOPS object oriented programming using python
#Classes and objects
class Person:
    name="kartik"
    age=23
    networth=10
    def info(self):
        print(f"{self.name} is a {self.age}")

a=Person()
# a.name="harleen"
# a.age=25
# print(a.name,a.age,a.networth)
a.info()    