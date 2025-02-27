what is constructor
what is self
how to call Constructor

# class Student :
#     def __init__(self):
#         print('constructor called')
#         print('self',id(self))
 

# obj=Student() 
# print(id(obj))     

# constructor is a special type of method that called automatically when object created of the class

class Student :
    def __init__(self,name,rol,marks):
        #self==it is a reference variable that holds address of current object of current class
        self.x=name
        self.y=rol
        self.z=marks
    def __init__(self):
        #self==it is a reference variable that holds address of current object of current class
           print('construter called==> last')
   
# obj=Student('kartikey',101,80) 
obj=Student()
print(obj)
obj.__init__()
# print(obj.x)
# print(obj.y)
# print(obj.z)



      