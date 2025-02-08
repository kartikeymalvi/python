# while True:
#     print("1 add\n 2 subtraction\n 3 division\n 4 multiplication\n  5 off")
#     n=int(input("enter your choise"))
#     if n==1:
#         x=int(input("enter 1st number"))
#         y=int(input("enter 2nd number"))
#         z= x+y
#         print('f addition of {x} and {y} is {z}')
#     elif n==2:
#         x=int(input("enter 1st number"))
#         y=int(input("enter 2nd number"))
#         z= x-y
#         print('f subtraction of {x} and {y} is {z}')
#     elif n==3:
#         x=int(input("enter 1st number"))
#         y=int(input("enter 2nd number"))
#         z= x/y
#         print('f division of {x} and {y} is {z}')
#     elif n==4:
#         x=int(input("enter 1st number"))
#         y=int(input("enter 2nd number"))
#         z= x*y
#         print('f multiplication of {x} and {y} is {z}')
#     elif n==5:
#             break
#     else:
#             print("enter valid number")    
while True:
    print("1 add\n 2 subtraction\n 3 division\n 4 multiplication\n  5 off")
    n=int(input("enter your choise"))
    p=(1,2,3,4)
    if n in p:
        x=int(input("enter 1st number"))
        y=int(input("enter 2nd number"))
        if n==1:
           z=x+y
           print(f'addition {x} and {y} is {z}')

    