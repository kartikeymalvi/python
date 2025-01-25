# tuple ==> collection of elements in a single object
# 1. tuple is immutable
# 2. tuple is ordered collection
# 3. tuple is represented in ()
# 4. tuple is indexing supported
# 5. tuple is slicing supported.
# tuple is faster compared to list because it is immutable and occupies less memory space
import sys
x=''
y=()
z=[]
print(sys.getsizeof(x)) 
print(sys.getsizeof(y))
print(sys.getsizeof(z))

tuple1=(10,20,30,40,50) 
print(type(tuple1))

#inbuilt functions for tuple
print(max(tuple1))
print(min(tuple1))
print(sum(tuple1))
print(len(tuple1))
print(id(tuple1))
print(type(tuple1))

#tuple methods
#1. count()
#2. index()
print(tuple1.count(10))
print(tuple1.index(50))
print(tuple1[-1])  #(gives last element of the tuple)