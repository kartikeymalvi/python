#  positional Argument
# keyword Argument

#Default Argument===>
# def fun_name(x=0,y=0,z=0):
#     p=x+y+z
#     print('hi')
#     return p
# print(fun_name(5,8,10))


# def fun_def(x=0,y=0,z=0):
#     z1=x+y+z
#     print(f'x={x} y={y} z={z}')
#     return z1
# x=fun_def(5,10,15)
# print(x)


# Variable length argument===>(* ARGS used to pass tuple in form of argument)(its datatype is tuple)
#  in this argument user can give many values as an argument
# def add(*n):
#     print(n)
#     print(type(n))
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
  
# w= add(8,8)    
# print(w)

# using taking input from user==>

# def addition(*x):
#     print(x)
#     sum1=0
#     for i in x:
#         for y in i:
#             sum1=sum1+y
#         return sum1 
# pri=eval(input('enter any tuple'))  
# fun=addition(pri) 
# print(fun)


#without nested for loop===>
# def add1(*n):
#     print(n)
#     print(type(n))
# x=eval(input('enter any tuple'))  
# result=add1(*x)
# print(result)  


# def add1(*n):
#     print(n)
#     print(type(n))
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# x=eval(input('enter any tuple'))  
# result=add1(*x)
# print(result)  


#Variable key-word argument===>(it is used to handle dict type)
#  imp==> diffrence btw (*args and **kwargs )
def show_my_details(**n):
    print(n)
    print(type(n))
    for k,v in n.items():
        print(f'my {k} is {v}')
show_my_details(name='kartikey',age=25,qualli='m.tech')  

#taking input from user in runtime====>
def show_my_details(**n):
    print(n)
    print(type(n))
    for k,v in n.items():
        print(f'my {k} is {v}')

x=eval(input('enter any dict'))
show_my_details(**x) 






