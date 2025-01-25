list1=[10,20,30,20.5,2,8,9]   #arrange in ascending order
list1.sort()
print(list1)
list1.reverse()
print(list1)

list1.pop()  # removes last element
print(list1)

list1.pop(2)  # removes element at index 2
print(list1)

list1.remove(20.5)  # removes first occurence of 20.5
print(list1)

list1.clear()  # removes all elements

print(list1) # [gives empty list]

#  # deletes the list
print(list1)  # [gives error as list is deleted]

list1=[10,20,30,20.5,2,8,9]
list2=list1.copy()  # copies the list

print(list2)  # [gives copied list]

print(id(list1),id(list2))  # [gives different memory address]


print(list1.count(20))  # [gives count of 20]

print(list1.index(8))
print(list1.index(10))