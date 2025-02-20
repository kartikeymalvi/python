# Topics in advance python
   
# HIGHER ORDER FUNCTION
# 1.map()===> Dictionary(key value pairs)
#    in this no of input element is always equal to output elements
#       [2,4,6,8]==[2,4,6,8]
# SYNTAX===>map(function-name,collection(string,tuple.dict,set etc.)) 
# 2nd Stntax ==> map(function-name,collection1,collection2,collection3---)
# Example===>
# def square(x):
#     return x**2
# li=eval(input('enter any numeric collection'))   
# res=map(square,li)
# print(res)
# print(list(res)) 
# def comp(x):
#     if x%2==0:
#         return x+1
#     else:
#         return x+2 
# li=[1,2,3,4,5,6,7,8,9,10]        
# res=map(comp,li)
# print(list(res)) 

# def add(x,x1,x2):
#     return x+x1+x2
# l1=[2,4,6]
# l2=[1,2,3]
# l3=[4,5,6,7,8]
# res= map(add,l1,l2,l3)
# print(list(res))    

# def fun(x):
#     if x%2==0:
#         return 'even'
#     else:
#         return 'odd'    
# li=eval(input('enter any numeric collection'))
# res=map(fun,li)
# print(res)
# print(list(res))


def power(x,x1):
    return x**x1
l1=[2,3,4]
l2=[2,3,4]
res=map(power,l1,l2)    
print(list(res))
      
# 2.filter()
# in this no of input element is always greater than or less than orequal to output elements according to condition in this at least one condition we have to declare to use it
# [2,4,6,8]==[,4,6,8]
# # SYNTAX===> filter(function-name,collection)
# def fun(x):
#     if x%2==0:
#         return x
# li=eval(input('enter any numeric collection'))
# res=filter(fun,li)
# print(res)
# print(list(res))

# def name(x):
#     if len(x)<=3:
#         return x

# li=eval(input('enter any string collection'))
# res=filter(name,li)
# print(list(res))


# # 3.reduce
#   in order to use reduce we have to import it and use from functools import reduce 
#SYNTAX==> functools.reduce(funcion-name,collection)
import functools
l1=[10,20,50,6,3,100,150]
def my_max(x,y):
    if x>y:
        return x
    else:
        return y
res=functools.reduce(my_max,l1)
print(res)    

# l1=[10,20,50,6,3,100,150]
# def my_max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# res=functools.reduce(my_max,l1)
# print(res)   

l1=[10,20,50,6,3,100,150]
def my_max(x,y):
     return x+y
res=functools.reduce(my_max,l1)
print(res)   






#==========
# Lambda FUnction
# decorators
# generators
# file handling
# oops