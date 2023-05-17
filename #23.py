s1={1,2,3,4,5,6}
s2={5,7,3,8,9}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
print(s1.intersection(s2))
print(s1.isdisjoint(s2))
s3=s1.symmetric_difference(s2)
print(s3)
print(s1.issuperset(s2))
print(s2.issubset(s1))
s2.discard(9)
print(s2)
# s2.remove(4)
# print(s2)
s4=s1.pop()
print(s4)




