#dictionary

dict={
    1:"Kartik",
    2:"pooja",
    3:"mihika",
    4:"soumya"
}
print(dict)
#print(dict[2]) # error throw karega
print(dict.get(2)) #does not show error show none
print(dict.keys())

for i in dict.keys():
    print(dict[i])
print(dict.values())


for i in dict.keys():
    print(f"the values corresponding to the key {i} is {dict[i]}")

print(dict.items())    

# methods in dictionary
dict2={
    5:"aananya",
    6:"mansvi"
}
dict.update(dict2)
print(dict)

dict3={}
print(dict3)


#removing last key value pair
dict.popitem()
print(dict)

del dict[1]
print(dict)



