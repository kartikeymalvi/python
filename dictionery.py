# Dict===>
# indexing in dictionary is not supported
# slicing in dictionary is not supported
# key must be unique
# value can be duplicate
# key is always in string format
# multable in nature
# represented in {} with comma (,)
# syntax==>
# d1=={key:value,key1:value1,key2:value2}

#IN BUILT FUNCTIONS FOR Dictionary=>
d1={'age':25,'city':'bhopal','name':'kartikey'}  #(in this min amd max is always mesured by alphabtical order)
print(max(d1))
print(min(d1))
print(len(d1))
print(type(d1))
print(id(d1))
print(' ')

#METHODS FOR DICTIONARY=>
#1. clear()
d1.clear()
print(d1)
print(' ')

#2.copy()
d2=d1.copy()
print(d2)
print(id(d1),id(d2))
print(d1,d2)
print(' ')

# 3.formkeys()
list1=['karikey','25','bhopal']
d3=dict.fromkeys(list1)
print(d3)
d3=dict.fromkeys(list1,10)  
print(d3) 
print(' ') 

dict1={'name':'kartikey','age':25,'city':'bhopal'}
# 4.get()  (it is used to get the value of the key) 


print(dict1.get('age')) #( it gives value of the key)
print(' ')


# 5.items()
print(dict1.items()) #(it gives key and value in tuple format)
print(' ')
# 6.keys()
print(dict1.keys())  #(it gives key in output)
print(' ')
# 7.values()
print(dict1.values()) #(it gives values in output)
print(' ')
#8. pop() 
print(dict1.pop('name'))  #(it removes key and value)
print(dict1)
print(' ')

#9. popitem()
print(dict1.popitem()) #(it removes last key and value) 
print(dict1) 
print(' ')

#10. setdefault()

dict2={'name':'lala','age':25,'city':'betul'}
dict2.setdefault('name','kartikey')

dict2.setdefault('new','guest')
print(dict2)
print(' ')

dict2.update({'name':'kartikey'})
print(dict2)






