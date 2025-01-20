# two types of indexing supports in python
# 1 ==>postive indexing
# 2 ==>negative indexing


# 1 ==>postive indexing ==>
#  it starts from 0
#    indexing stops =(n-1)
# it is used to findout first object


# 2. ==>2 ==>negative indexing==>
#  it starts from -1
#  indexing stops =(n+1) ==> (-2+1)=-1
# it is used to findout last object 


#syntax==> indexing is used on collections 
# collection.index('obj')

#indexing in list
str1= 'python'
print(str1.index('p')) 
# str2= 'python'
# print(str2.index('p',0,1))  (throws error) 

str2='kartikey'
print(str2[0])
print(str2[1])
print(str2[2])
print(str2[3])


mylist=[10,20,30,'kartikey',50]
# print(mylist.index(10))  (gives index number in output)
# print(mylist.index('kartikey'))
# print(mylist.index('kartikey',0,4))#(collection.index('objname',startpoint,endpoint))
print(mylist[3])  # (gives value in output)


#indexing in tuple
mytuple=(10,20,30,'kartikey',50)
print(mytuple.index('kartikey'))
print(mytuple.index('kartikey',1,4))  #(collection.index('objname',startpoint,endpoint))
print(mytuple[3])

