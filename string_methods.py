# STRING METHODS ===>
# 1. lower()
# 2.upper()
# 3.title()
# 4.capitalize()
# 5.swapcase()
# (diffrence btw find and index)
# 6.find()  (imp-interview ques ) (in this we find the index of the object but it can not throw error when the element is not present) 
# 7.index() (imp-interview ques )  (in this we find the index of the object but it will throw error when the element is not present)
# 8.join() (imp-interview ques )
# 9.split() (imp-interview ques return type list)

str1='I love python'
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.capitalize())
print(str1.swapcase())
print(str1.find('z'))
# print(str1.index('z'))
print(str1.split( ))
print(str1.split('o'))
print(str1.split('o',2))
str2=['kartikey','malviya','age','25']
print((','.join(str2)))  # (it add (,) after every object and join them we can change it according to use it return single object)
str3=(('').join(str2))
print(('-'.join(str2)))
print((' '.join(str2)))
print(type(str3))
print(str1.count('o')) #count the number of object in the collection
  