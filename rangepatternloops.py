
# display pairs whose sum is 5 in the range of 1 to 5 


for j in range(1,6,1):
    for i in range(1,6,1):
        if(j+i==5):
            print(f" j Pair is: ({j}, {i})")
    print()


# display even number range from 1 to 10 

for j in range(1,11,1):
    n=j
    if ( n%2==0):
        print(n) 

for j in  range(1,11,1):
    n=j
    if n%2 != 0:
        print("it is not even",n)

# print multiplication table of 1 to 10
 
for j in range(1,11,1):
    for i in range(1,11,1):
        print(f"{j} * {i} = {j*i}")
    print()


    # factorial number range from 1 to 5


print("factorial number range from 10 to 15")
for j in range(10,16,1):
    n=j
    fact=1
    for i in range(n,0,-1):
           fact=fact*i
           print(f"factorial of {i} is:{fact}")

# print prime number range from 1 to 10

for j in range(1,11,1):
    n=j
    count=0
    for i in range(1,n+1,1):
        if(n%i==0):
            count=count+1
    if(count==2):
        print(f"{n} is prime number")

 # display perfect number range from 1 to 10000

for j in range(1,10001,1):
    n=j
    sum=0
    for i in range(1,n,1):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        print(f"{n} is perfect number")

#  display palindrome number range from 100 to 150

for j in range(100,151,1):
    n=j
    temp=n
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(temp==rev):
        print(f"{temp} is palindrome number")



 
