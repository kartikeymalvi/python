# python has two object types ==>
# 1. immutable=>( int,str,tuple,frozenset) (can not be changed)
# 2. mutable =>(list,dict,set) (can  be changed)
# immutable===>
# 1.integer
x=10
y=10
print(id(x),id(y))

# 2.=> string
a='kartikey'
b='kartikey'
print(id(a),id(b))

# 3. ==>Tuple 
x1=(10,20,30,'kartikey')
y1=(10,20,30,'kartikey')
print(id(x1),id(y1))

#Mutable==>

#1.list ==>

l1=[10,20,30,'kartik']
l2=[10,20,30,'kartik']
print(id(l1),id(l2))

#2.  dictionary===>

d1= {'name':'kartikey','age':25,'city':'bhopal'}
d2= {'name':'kartikey','age':25,'city':'bhopal'}
print(id(l1),id(l2))

#3. set===>
s1={ 10,20,30, 'kartik'}
s2={ 10,20,30, 'kartik'}
print(id(s1),id(s2))

#4 Frozenset ==>  this is multable but allocates diffrent memory address
f1= frozenset({ 10,20,30, 'kartik'})
f2= frozenset({ 10,20,30, 'kartik'})
print(id(f1),id(f2))

