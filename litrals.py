# litral types ==>
#  x (variable)=10(constant value)==is called litrals
  
#   types ==>
#1.numeric ==> integer(10,20,2) ,float(2.2.2.5) , 
 #(not used in webdev.)complex(x(real)+j(imagenary part)j)

a=10  #(integer)
print(type(a))

a1=10.2  #(float)
print(type(a1))

a3=5+3j  #(complex)
print(type(a3))

# 2. string==>  collection of characters 
# 1. ''  (used to create single line string)
x='n'
print(type(x))
# 2." "  (used to create single line string)
x1="n"
print(type(x1))
# 3.''' ''' (used to create multi-line string)
x3 = ''' x  
            *
           * * 
          * * * '''
print(x3) 
x2='''n'''
print(type(x2))

#3. Boolean (true false)

o=True
print(o)
print(type(o))
o1=False
print(o1)
print(type(o1))

#list ==> (collection of objects) 
# represented in [] in (,) seprated object
my_list =[10,a,30.2,'kartikey',50,[1,2,3]]
print(type(my_list))

# 4. tuple ===> (collection of objects )
# represented in () in (,) seprated object
my_tuple =(10,a,30.2,'kartikey',50,(1,2,3))
print(type(my_tuple))

#5 .  dictionary  ( collection of ('key':'value')=(1 pair)  pairs)
# represented in {} in (,) seprated object
my_dict ={ 'name':'kartik','age':25,'city':'bhopal'}
         # ( 1st object) ,(2nd object), (3rd object)
print(type(my_dict))

#6.  set (collection of unique object we can not assign same value and output order is not fixed )
#  represented in {} in (,) seprated object
my_set ={10,20,30,'kartik','rey',10.5,10,20,'rahul'}
print (my_set)
 
# 7. Frozen-set (immutable set)
my_fset = frozenset({10,20,30,'kartik','rey',10.5,10,20,'rahul'})
print (my_fset)



         




