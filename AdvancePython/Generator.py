# def even(x):
#     i=0
#     while i<=x:
#         if i%2==0:
#             print(i)

          
#         i=i+1 
# even(10)

# def new():
#     return 'lala'
# x=new()
# print(x)
# print(type(x))  


#Generator is a special type of function that can be use to generante iterator object
# ==>insted of return keyword yield keyword used.

# def new1():
#     yield 10
# x=new1() 
# print(x)   
# print(list(x))
# print(x.__next__())
# print(next(x))

# def even(x):
#     i=0
#     while i<=x:
#         if i%2==0:
#             yield i
#         i=i+1
# res=even(10)
# print(res)  
# print(list(res)) 
# x=next(res)           
# y=next(res)           
# z=next(res)           
# print(x,y,z) 
def even(x):
    i=0
    while i<=x:
        if i%2==0:
            yield i
        i=i+1
res=even(10)
# print(res)  
# print(list(res))      
print (next(res))  
print (next(res))  
print (next(res))  
  


