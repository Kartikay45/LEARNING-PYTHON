# list
l=[3,4,5,"harry",True]
print(l)
print(type(l))
print(type(l[3]))
print(type(l[4]))

if "arry" in l:
    print("Yes")
else:
    print("No")

print(l[:])

lst=[i*i for i in range(4)]
print(lst)

st=[i*i for i in range(100) if i%2==0]
print(st)


