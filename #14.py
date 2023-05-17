def sum(a,b):
    print(a+b)

 
# tuple in functions
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    #print("average is:-",sum/len(numbers))
    #return 7
    return sum/len(numbers)
    


c=average(5,6,7,8)
print(c)

#dictionary in function
def name(**oggy):
    print("Hello",oggy["fname"],oggy["lname"],oggy["mname"])

name(mname="Buchaman",fname="Aggarwal",lname="Hat")    
