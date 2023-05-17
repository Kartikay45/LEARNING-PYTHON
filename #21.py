# factorial 4= 4*3*2*1
# factorial 5=5*4*3*2*1

# factorial= n* factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))
print(factorial(4))    

#fibonnaci
# f0=0
# f1=1
# f2=f1 + f0

# f(n) = f(n-2) +f(n-2)
#f0=0
#f1=1

def f(q):
    if (q<0):
        print("incorrect input")
    elif(q==0):
        return 0
    elif(q==1 or q==2):
        return 1 
    else:
        return f(q-1) + f(q-2)   
    
    
        #return f(q-1) + f(q-2)
    
print(f(5)) 
print(f(6))




