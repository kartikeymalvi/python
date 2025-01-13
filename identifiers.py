# identifier is a name that can be used to identify python objects..
# objects are ==> (variable,function name,class name, module,package,library)
x=10
# 1xys=50 throws error
# s=10x throws error
xyz=10
# 1xyz=10x throws error

number=50
NUMBER=55
_number=60
print(number+NUMBER+_number)


# case sensitive

# z=20
# print(Z)  Throws error because python is case sensitive
z=20
print(z)

# combination of digit and alphabet and underscore (_) for declaring variable
_123xyz=1
_1x2y=2
x_123=3
x12_3=4
print(_123xyz)
print(_1x2y)
print(x_123)
print(x12_3)

# DO not use space 
# x y=10 throws error
 
name="kartikey Malviya"
age=25
print("hello",name)
print("Name =",name)
# print(id(quali)) throws error because quali is not declared
print(id(name))
print(id(age))

