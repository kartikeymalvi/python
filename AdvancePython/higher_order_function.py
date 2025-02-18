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
def comp(x):
    if x%2==0:
        return x+1
    else:
        return x+2 
li=[1,2,3,4,5,6,7,8,9,10]        
res=map(comp,li)
print(list(res))           
      



# 2.filter()
# in this no of input element is always greater than or equal to output elements according to condition
# [2,4,6,8]==[,4,6,8]
# # 3.reduce
#    in this no of input element is always equal to output elements
#==========
# Lambda FUnction
# decorators
# generators
# file handling
# oops