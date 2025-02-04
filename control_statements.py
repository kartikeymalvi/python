# CONTROL STATEMENTS





# 1.CONDITIONAL STATEMENTS==>

 #order to place if elif else==>

#  1.if statements
#  2.elif statements
#  3.else statements

#===========================
# 1.if ==>
# syntax==>
# if (condition):
#     statements---1
#     statements---2....

# 2.if-else
# if (condition):
#     statements---1
#     statements---2....
# else:
#     statements---1
#     statements---2....

# x = int(input ("Enter any number"))
# if (x%2==0):
#     print("given number is even")
# else:
#     print("given number is odd")

# num1=int(input("enter first number"))    
# num2=int(input("enter second number"))    
# if(num1>num2):
#     print( f" {num1} is greater")
# else:
#     print(f'{num2} is greater')    

# age=int(input("enter your age"))
# if(age>=18):
#     print("you can vote now")
# else:
#     print("no boy you are not eligible for vote now ")  

   #find the greatest value in given three numbers
# a=int(input("enter 1st number"))
# b=int(input("enter 2nd number"))
# c=int(input("enter 3rd number"))
# if (a>b and a>c):
#     print(f'{a} is greater than {b} and {c}')
# else:
#     if(b>c and b>a):
#         print(f'{b} is greater than {c} and {a}')
#     else:
#         print(f'{c} is greater than {a} and {b}')





# 3.if-elif===>
# syntax===>
# if(condition):
#     ------statements.....
# elif(condition):
#     ------statements.....
# elif(condition):
#     ------statements.....
# else:
#         ------statements.....
# x=int(input("enter 1st number:"))
# y=int(input("enter 2nd number:"))
# z=int(input("enter 3rd number:"))
# if( x==y and y==z):
#     print('all values are equal')
# elif( x>y and x>z):
#     print(f'{x}is greater ')     
# elif(y>z and y>x):
#     print(f'{y} is greater')
# elif(z>x and z>y):
#     print(f'{z} is greater')   
# elif(x==y):
#     print(f'{x} and {y} are equal')
# elif(y==z):
#     print(f'{y} and {z} are equal')  
# elif(z==x):
#     print(f'{z} and {x} are equal') 

#while loop syntax====>

           
# n=int(input("enter number"))
# i=1
# while i<=n:
#     if i<n:
#         print(i,end=',')
#     else:
#         print(i)
#     i=i+1
# print("Hello")      

#count digit program===>

# number=int(input("enter numbers to find digits"))
# digit=0
# while number>0 :
#     digit=digit+1
#     number=number//10
# print(digit)
# print(number) 


#add power===>

# num=int(input("enter numbers "))
# sum=0
# while num>0:
#     last_digit=num%10
#     sum=sum+last_digit**3
#     num=num//10
# print(sum)
# print(num)    

#armstrong number====>

number=int(input("enter numbers to find armstrong number"))
x=y=number
digit=0
while number>0 :
    digit=digit+1
    number=number//10
sum=0
while y>0:
    last_digit=y%10
    sum=sum+last_digit**digit
    y=y//10
if x==sum:
    print(f'{x} is armstrong')    
else:
    print(f'{x} is not armstrong')   

    #palindrome number===>
     
    





