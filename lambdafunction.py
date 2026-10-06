
# lambda function without arg and return

sayhello=lambda:print("hello")
sayhello()

# lambda function with parameter and without return
firtsname= lambda fname:print("my first name is ", fname)
firtsname("gandla")

# lambda function without arg and with return

displayname=lambda:"hello niharika"
print(displayname())

# lambda function with arg and with return

displayName=lambda fname:"My Name is "+fname
print(displayName("Niharika"))

sum=lambda num1,num2: "The sum of num1 and num2 is={num1+num2}"
print(sum(10,20))

# lambda always retuns something exp or value
sayhello=lambda:print("hello")
print(sayhello())

# lambda with conditions

EvenOrOdd=lambda:"Even" if 5%2==0 else "odd"
print(EvenOrOdd())

# lambda with arg and return
EvenOrOdd=lambda n1:"Even" if n1%2==0 else "odd"
print(EvenOrOdd(10))