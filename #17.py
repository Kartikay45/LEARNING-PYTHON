countries=("spain","russia","japan","india")

temp=list(countries)
temp.pop(2)
print(temp)
countries=tuple(temp)
print(countries)
tuple1=(1,2,3,4,5,3,4,5,3,4,4,3)
#res=tuple1.index(2)
res=tuple1.index(4,2,8)
print(res)