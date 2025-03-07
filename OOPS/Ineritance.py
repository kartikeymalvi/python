# INERITANCE=====>parent chlid relation of class
# advantage==>
# Code Reusability
# Time saving
# reduce redendency
# class A:
#     x=10
#     y=20
#     def home(self):
#         print('i have a home')
#     def car(self):
#         print('i have a car')
# class B(A):
#     def newhome(self):
#         print('i have new home')    
# obj=B()
# obj.home()
# print(B.x)
# obj.car()
# obj.newhome()  

# TYPES OF INHERITANCE====>
# 1.SINGLE INHERITANCE==>
# in this chlid class inherits properties of parent class===>
# class Parent:
#     x=10
#     def home(self):
#         print('this is parent home')
# class Chlid(Parent):
#     y=20
#     def newhome(self):
#         print('this is child home') 
# obj=Chlid()
# print(Chlid.x)
# obj.Parent()
# obj.Child() 
# print(Child.y)    


# Method overriding in python->
# class Parent:
#     x=10
#     def home(self):
#         print('this is parent home')
# class Chlid(Parent):
#     y=20
#     def Home(self):
#         super().home()
#         print('this is child home') 
# obj=Child()
# obj.Home()
# 2.MUlTIPLE INERITANCE==>
# in this chlid class inherits properties of multiple parent classes
# parent1     parent2
#    |           |
#    |___________|
#          |
#        chlid
# MRO=(Method resolution order)
# in this multiple parents class is define priority by which class properties gets  inherited into child   (parent1,parent2) in child class inherits parents1 properties first and after parent2
       
# 3.MUlTILEVEL INERITANCE===>
#     Grand-parent
#          |
#        parent
#          |   
#        chlid


# class Grandparent:
#     def Home(self):
#         print('Grand--parent')
# class Parent(Grandparent):
#     def Home1(self):
#         print("parent home")
# class Child(Parent):
#     def Home2(self):
#         print('child-home')   
# obj=Child()
# obj.Home()
# obj.Home1()                   
# obj.Home2()                   

# 4.Hierarichical INERITANCE==>in this inheritance propertities of parent goes to the multiple child classes

# class Parent:
#     def Home(self):
#         print('parent class')
# class Child(Parent):
#     def Home1(self):
#         print('child 1 class')
# class Child2(Parent):
#     def Home2(self):
#         print('child 2 class')
# obj=Child2()
# obj.Home()
# obj1=Child()
# obj1.Home1()       



# HYBRID-INERITANCE===>
class Parent:
    def home(self):
        print('parent class')
class Child1(Parent):
    def home(self):
        print('from child 1')  
class Child2(Parent):
    def home(self):
        print('from child 2')   
class Child3(Child1,Child2):
    def new(self):
        print('from child3')
obj=Child3()
obj.home()                          
print(Child3.__mro__)

