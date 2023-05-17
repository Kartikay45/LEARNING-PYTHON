print("hello")
for i in range(12):
    if(i==10):
        break
    print("5 X",i+1,"=",5*(i+1))

for i in range(12):
    if(i==10):
        print("ab skip hoga")
        continue
    print("5 X",i+1,"=",5*(i+1)) 

# emulating do while loop
i=0
while(True):
    print(i)
    i=i+1
    if(i==100):
        break       

