# s=int(input("enter the value"))
# n=int(input("enter the value"))
# for i in range(s,n+1,1):
#     if i%2==0:
#         print(f"{i} is even number")

#ood numbers without 
# s=15
# n=int(input("enter the value"))
# for i in range(s,n-1,-1):
#     if i%2==1:
#         print(f"{i} is odd number")

#write code for divisible by 5
# s=15
# n=int(input("enter the value"))
# for i in range(s,11,1):
#     if i%5==0:
#         print(f"{i} is divisible by 5")

#count the even numbers 1 to 5
# count=0
# for i in range(1,6,1):
#     if(i%2==0):
#         count=count+1
# print(f"the even numbers b/w 1 to 5 is:{count}")

#display the sum of odd numbers the range of 5 to 10
# sum=0
# count=0
# for i in range(5,11,1):
#     if(i%2==1):
#         sum=sum+i
# print("sum of odd numbers are ",sum)

#display the sum of odd numbers the range of 15 to 5
# sum=0
# for i in range(15,4,-1):
#     if(i%2==1):
#      sum=sum+i
#      print("sum of odd numbers are ",sum)

#find the factors of 6
# factorial=int(input("enter factorial numbers "))
# for i in range(1,7,1):
#     if(factorial%i==0):
#         print("the factorial numbers  are:",i)

#count the factors 
# count=0
# fact=int(input("enter the value"))
# for i in range(1,7,1):
#     if(fact%i==0):
#         count=count+1
# print("the count is",count)

#prime number
p=int(input("enter the value"))
count=0
for i in range(1,p+1,1):
     if(p%i==0):
          count=count+1
if(count==2):
    print("it is a prime number")
else:
     print("it is not a prime number")

#find the sum of factors of given number
p=int(input("enter the value"))
sum=0
for i in range(1,p,1):
     if(p%i==0):        
        sum=sum+i
print(sum)     
if(sum==p):
    print("it is aperfect number")
else:
    print("it is not a perfect number")

