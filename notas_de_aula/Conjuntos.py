a = {1, 2, 3}
print(type(a))
a = set('coddd3r')
print(a)
##Não aceita repetição ####

print(3 in a)
print('d' in a)

print({1,2,3} == {3,2,1,3})

c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)

print(c2<=c1)