'''print(15+7)
print(15-7)
print(15*7)
print(15/7)
print(15//7)
print(15%7)
print(15**7)'''

#basic calculator program
print("enter 2 integers numbers\n a\n b\n")

a=int(input())
b=int(input())

print("chose the operand:-\n +\n -\n *\n /\n")
c=input()

if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)
else:
    print("default input")           
    
