#Exeptional handling
#try - execpt
a=input("enter the integer number")

print(a)

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except:
    print("invalid input")
finally:    
    print("end of program")        

