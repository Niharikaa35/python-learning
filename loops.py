

for i in range(1, 4, 1):
        print("hello")

for i in range(1, 5, 1):
    print("hello")

for i in range(2,17,3):
      print(i)

for i in range(3,0,-1):
    print(i)

for i in range(100, 0,-10):
    print(i)

#sum of first 3 numbers
sum=0
n=5
for n in range(1,n+1,1):
     sum=sum+n
print("sum of first 3 numbers is:", sum)
print(f"sum of first {n} numbers is {sum}")

#find the avg of first n natural numbers
n=int(input("enter the value of n:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
avg=sum/n
print(f"average of first {n} natural numbers is {avg}")


sum=0
for i in range(1,4,1):
     sum=sum+10
     print(f"the sum value is {sum}")

n=int(input("enter the value of n:"))
sum=0
for i in range(1,n+1,1):
     sum=sum+i
print(f"the sum of first {n} natural numbers is {sum}")


#mulitiplication of two  table 
n=int(input("enter the value of n:"))
for i in range(1,11,1):
     print(f"{n}x{i}={n*i}")

#factorial of a number
n=int(input("enter the value of n:"))
factorial=1
for i in range(n,0,-1):
     factorial=factorial*i
print(factorial)

     