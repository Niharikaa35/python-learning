def first_function_Eg():
    print("Hello, Function!")

# without  parameter and without return value

def sum_of_two_numbers():
    a=10
    b=20
    c=a+b
    print(f"sum of a , b  is {c}")
sum_of_two_numbers()


# write the code to display the smallest number from given three numbers
def smallest_number():
 n1=10
 n2=20
 n3=30

 if n1<n2 and n1<n3:
    print(f"{n1} is smallest number")  
 elif n2<n1 and n2<n3:
    print(f"{n2} is smallest number")
 else:
    print(f"{n3} is smallest number")

smallest_number()


# with  parameter and with arguments 
def name(name):
   print(f"Hello, {name}!")
name("Niharika")

# write the logic to check whether given number is even or odd
def even_odd(num):
   if num%2==0:
        print(f"{num} is even number")
   else:
      print(f"{num} is odd number")
even_odd(13)

# write the logic to check average of three numbers 
def average_of_three_numbers(n1,n2,n3):
   avg=n1+n2+n3/3
   print(f"average of three numbers is {avg}")
average_of_three_numbers(10, 20, 30)


def name():
   name="niha"
   return name

myname=name()
print(f"my name is {myname}")

# factorial of a number

def factorial_of_number():
   n=int(input("enter the value"))
   fact=1
   for i in range(1,n+1,1):
      fact=fact*i
   return fact
factorials=factorial_of_number()
print(f"factorial of number is {factorials}")

# write the code for the return the sum of even numbers in the range of 1 to 10
def sum_of_even_numbers():
    sum=0
    for i in range(1,11,1):
      if i%2==0:
         sum=sum+i
    return sum
sum_of_evens=sum_of_even_numbers()
print(f"sum of even numbers is {sum_of_evens}")

def display_name(myname):
   return f"my name is {myname}"
print(display_name("niha"))

# to check given number is prime or not
num=int(input("enter the value"))
def prime_or_not(num):
   if num>1:
      for i in range(2,num):
         if num%i==0:
            return f"{num} is not a prime number"
      else:
         return f"{num} is a prime number"
print(prime_or_not(num))
