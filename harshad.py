x=int(input('enter number'))
n=x
sum=0
while x>0:
    last_digit=x%10
    print(last_digit)
    sum=sum+last_digit
    
    x=x//10

if n%sum==0:
    print(f'this number is harshad {sum}') 
else:
    print('this is not harsad number')       

# #neon number
# n = int(input('Enter a number: '))

# # Step 1: Find the square of the number
# square = n * n

# # Step 2: Sum the digits of the square
# sum_of_digits = 0
# temp = square  # Store the value in a temp variable to process

# while temp > 0:
#     sum_of_digits += temp % 10  # Extract last digit and add to sum
#     temp //= 10  # Remove last digit

# # Step 3: Check if the sum equals the original number
# if sum_of_digits == n:
#     print(f'{n} is a Neon Number.')
# else:
#     print(f'{n} is not a Neon Number.')
# n = int(input('Enter a number: '))

# # Step 1: Find the square of the number
# square = n * n

# # Step 2: Sum the digits of the square
# sum_of_digits = 0
# temp = square  # Store the value in a temp variable to process

# while temp > 0:
#     sum_of_digits += temp % 10  # Extract last digit and add to sum
#     temp //= 10  # Remove last digit

# # Step 3: Check if the sum equals the original number
# if sum_of_digits == n:
#     print(f'{n} is a Neon Number.')
# else:
#     print(f'{n} is not a Neon Number.')



