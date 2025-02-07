# Break===>exit from loop
n=int(input("enter number"))
i=1
while i<=n:
    if i==6:
        break
    print(i)
    i=i+1
print("hello")        

#continue====>skip current itration
n1=int(input("enter number"))
i=1
while i<=n1:
    if i==6:
        i=i+1
        continue
    print(i)
    i=i+1
print("hello")  



# pass===>skip current block(used to currect the synthatical errror)
n2=int(input("enter number"))
i=1
while i<=n2:
    if i==6:
        
        pass
    print(i)
    i=i+1
print("hello")