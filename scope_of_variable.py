# two types of Scope present in python===>
#1.Global variable
#2.Local variable
# if we want to make any variable global we have to use global keyword
   
# x=10    #Global variable
# def add():
#     y=20   #Local variable
#     print(x) #we can acess here because x has global scope
#     print(y)
# add()
# print(x)    
# #print(y) #this is y can noe acccessed here beacuse it has local scope  



# x=10    #Global variable
# def add():
#     global y
#     y=20   #Local variable
#     print(x) #we can acess here because x has global scope
#     print(y)
# add()
# print(x)    
# print(y) #this is y is  acccessed here beacuse it has global scope decalred with global keyword

a=10
def new():
    global a
    print(a)
    a=20
    print(a)
new()
print(a)    

#to call any global variable that having same name into the another block of code we use globals()
#         method globals() ['x']  ex==>
y=10  #global variable
def loc():
    global b,c#making b global variable
    b=100
    c=200
    y=20   #local variable
    print("value of global variable y :",globals()['y'])
    print("value of local variable y :",y)
    print("value of local variable b :",b)
    print("value of local variable c :",c)
loc()
print("value of global variable y :",y)    
print("value of global variable b :",b)
print("value of global variable c :",c)

