# swap two numbers

import string
from turtle import write


a=10
b=20
print(f"Before swapping a={a} and b={b}")
a=a-b
b=a+b
a=b-a
print(f"After swapping a={a} and b={b}")

# display largest number from three numbers
n1=15
n2=20
n3=10
if n1>n2 and n1>n3:
    print(f"{n1} is largest number")
elif n2>n1 and n2>n3:
    print(f"{n2} is largest number")
else:
    print(f"{n3} is largest number")


# write code to check whetether given value is uppercase or lower case or not an alpabet

a=str(input("Enter the name"))
if a>="A" and a<="Z" or a>="a" and a<="z":
    print(f"{a} is an alphabet")
else:
    print(f"{a} is not an alphabet")    

# print odd numbers in the range of 1 to 10
for i in range(1,11,1):
    if(i%2==1):
        print(f"{i} is odd number") 

# check given number is perfect number or not
n=int(input("enter the value")) 
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")

# display the average of digits of given number(4568)
n=4568
sum=0
count=0
while n>0:
    digit=n%10
    sum=sum+digit
    count=count+1
    n=n//10
average=sum/count
print(f"Average of digits of 4568 is {average}")


# 513212345
#  5432345
#   54345
#    545
#     5


for j in range(1, 6):

    # spaces
    for s in range(1, j):
        print(" ", end="")

    # decreasing numbers
    for k in range(5, j - 1, -1):
        print(k, end="")

    # increasing numbers
    for i in range(j + 1, 6):
        print(i, end="")

    print()


# find the avg of prime numbers in the range of 1 to 10

for j in range(1, 11):
    n = j
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(f"{n} is a prime number")


# write the code to skip the 0 from the given number 10405
n = 10405
if n > 0:
    digit = n % 10
    if digit != 0:
        print(digit)
    n = n // 10

