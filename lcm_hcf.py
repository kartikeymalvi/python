x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
max_no=max(x,y)
while True:
    if max_no%x==0 and max_no%y==0:
        break
    max_no=max_no+1
print(f' lcm of {x} and {y} is {max_no}')    

# hcf and palindrome using eval()