#Lambda Funtion====>
# A function that does not have any name it is also called as annonymus function
# Here,function define with lambda key-word insted of def
# it takes n number of arguments and execute only single line of expression
#Syntax===> lambda args:expression
# x=lambda x,y:(x+y)
# p=int(input('enter 1st number'))
# q=int(input('enter 2nd number'))
# print(x(p,q))
# x=lambda x,y:print(x+y)
# p=int(input('enter 1st number'))
# q=int(input('enter 2nd number'))
# x(p,q)

# To use lambda function with if-else===>
# Syntax==>lambda arguments:result-of-if if(condition)else(result of else)
# n=int(input('enter number to find even or odd'))
# check_number=lambda x:'number is even' if(x%2==0) else 'number is odd'
# print(check_number(n))

# x1=int(input('enter number'))
# check_number1=lambda x1:'number is positive' if(x1>0) else ('number is negative' if(x1<0) else 'number is zero')
# print(check_number1(x1))

# To use lambda function with for-loop===>
# Syntax==>
# y=lambda p:[i for i in range (p)]
# p=int(input('enter numbers'))
# print(y(p))

x=lambda p,q:[[r for r in range(p)]  for i in range(q)]
p=int(input('enter number'))
q=int(input('enter 2nd number'))
print(x(p,q))