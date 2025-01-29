#frozenset===>
# 1.collection of unique elemets
# 2.unorderd
# 3.indexing not supported
# 5.slicing not supported
# 6.immutable in nature
s='kartikey'
l=[10,20,30,40,50]
t=(30,50,80,70)
d={'name':'kartikey','quali':'b.tech'}
s1={'kartikey','neeraj','john'}
x=frozenset(s)
print(x)
print(type(x))
print(' ')

X={10,20,30,40}
Y={10,5,7,30,40,50}
A=frozenset(X)
B=frozenset(Y)
print(X.union(Y))  #union (removes duplicates and print only one time)

print(X.intersection(Y))  #intersection  ( print only  duplicates )

print(X.difference(Y))  #difference(print only unique elements)

print(X.symmetric_difference(Y))

print(X.isdisjoint(Y))  #in this it checks common elements if yes it returns falue in boolean
print(' ')
sub={1,2,3,4,5}
sub1={1,2,3,4,5,8,9,10}

print(sub.issubset(sub1))

print(sub.issuperset(sub1))
