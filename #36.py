#constructor
class Person:

    def __init__(self,n,o):
        print("hey i am a person")
        self.name=n
        self.age=o
    # name="kartik"
    # age=23

    def info(self):
        print(f"{self.name} is  {self.age} years old")

a=Person("Kartik",23)   
b=Person("Pooja",53)     
#print(a.name)
a.info()
b.info()