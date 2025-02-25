# #Decoraor===>Special type of igher order function that can take function as an argument
# and it also return function(where we change the behaviour)

# def outer_fun(fun1):
#     def inner_function():
#         print('before modification')
#         fun1()
#         print('after modification')
#     return inner_function
# def fun():
#     print('this is from main function')
# res=outer_fun(fun)
# res()            

# def outer_fun(fun1):
#     def inner_function():
#         print('before modification')
#         fun1()
#         print('after modification')
#     return inner_function
# @outer_fun
# def fun():
#     print('this is from main function')
# fun()    

def outer_fun(fun1):
    def inner_function(r,s,t):
        r=r+10
        s=s+20
        t=t+30
        a=fun(r,s,t)
        print(a)
    return inner_function 
@outer_fun
def fun(x,y,z):
    return x+y+z

x=10
y=20
z=30
fun(x,y,z)           