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
class Parent1:
    def Home(self):
        print('parent1 home')
class Parent2:
    def Home(self):
        print('parent2 home')        
class Child(Parent2,Parent1):
    def car(delf):
        print('child car')
obj=Child()
obj.Home ()       
# 3.MUlTILEVEL INERITANCE===>
#     Grand-parent
#          |
#        parent
#          |   
#        chlid


class Grandparent:
    def Home(self):
        print('Grand--parent')
class Parent(Grandparent):
    def Home1(self):
        print("parent home")
class Child(Parent):
    def Home2(self):
        print('child-home')   
obj=Child()
obj.Home()
obj.Home1()                   
obj.Home2()                   

# 4.Hierarichical INERITANCE==>
