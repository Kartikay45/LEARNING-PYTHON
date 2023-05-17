# getters setters
# inheritance
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"the name of the employee: {self.id} is {self.name}") 

class Programmer(Employee):
    def showlanguage(self):
        print("default language is python")      



e=Employee("Rohan Das",420)   

e.showDetails()
#e2=Employee("Rohan Das",420)   
e2=Programmer("harry",4100)
e2.showlanguage()
e2.showDetails()



