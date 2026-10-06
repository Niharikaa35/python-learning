#1.Add two numbers
add = lambda a, b: a + b

print(add(10, 20))    #o/p:30
#_________________________________________________________________________________________________________________________________________#
#2.Subtract two numbers
sub = lambda a, b: a - b
print(sub(10, 4))   #o/p:6
#________________________________________________________________________________________________________________________________________#
#3.Find square of a number
square = lambda x: x * x
print(square(5))   #o/p:25
#____________________________________________________________________________________________________________________________________________#
#4.Check even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(8))
print(check(7))     
#______________________________________________________________________________________________________________________________________________#
#5.Find bigger number
big = lambda a, b: a if a > b else b
print(big(10, 20))  #o/p:20
#_______________________________________________________________________________________________________________________________________________#
#6.Find smaller number
small = lambda a, b: a if a < b else b
print(small(10, 20))    #O/P:10
#_________________________________________________________________________________________________________________________________________________#
#7.Add 10 to a number
add10 = lambda x: x + 10
print(add10(5))     #O/P:15
#__________________________________________________________________________________________________________________________________________#
#8.CUBE OF A NUMBER
cube = lambda x: x * x * x
print(cube(3))    #O/P:27
#__________________________________________________________________________________________________________________________________________________#
#9.CHECK POSITIVE OR NEGATIVE
check = lambda x: "Positive" if x > 0 else "Negative"
print(check(10))
print(check(-5))
#_________________________________________________________________________________________________________________________________________________#
#10.Convert Celsius to Fahrenheit
temp = lambda c: (c * 9/5) + 32
print(temp(20))         #o/p:68.0
#__________________________________________________________________________________________________________________________________________________#
#11.Get last digit of a number
last = lambda x: x % 10
print(last(12345))     #o/p:5
#_______________________________________________________________________________________________________________________________________________#
#12.Mulitiply two numbers
multiply = lambda a, b: a * b
print(multiply(4, 5))   #o/p:20
#_________________________________________________________________________________________________________________________________________________#
#13.Divide two numbers
divide = lambda a, b: a / b
print(divide(10, 2))   #o/p:5.0
#________________________________________________________________________________________________________________________________________________#
#class problems
#1.lambda fonction without input and without return
#declaration
sayhello=lambda:print("hello")
#invoking
sayhello()   #hello
#____________________________________________________________________________________________________________________________________________________________#
#2.lambda fonction with input and without return
#syntax
   #lambda parameter:expression
#declaration
displayname=lambda fname:print("My name is ",fname)
# #call or invoke
displayname("Hero") #argument
#________________________________________________________________________________________________________________________________#
#3.lambda fonction without input and with return
#lambda:"value to be returned"
#decleration
# displaymsg = lambda: "hello hero"
# #Invoking
# print(displaymsg())
#___________________________________________________________________________________________________________________________________#
#4.lambda fonction with input and with return
#declaration
# displayname = lambda fname: "my name is " + fname
# #Invoking 
# print(displayname("Innomatics"))
#5.
addtwo= lambda n1,n2:f"sum={n1 + n2}"
print(addtwo(10,20))
#lambda expr always returns  expr or none
sayhello = lambda:print("hello")
print(sayhello())
#______________________________________________________________________________________________________________________________________#
#lambda function usinf conditional stmts
#lambda function without input and with return
#1.check given number is even or odd.
checkeven = lambda:"even" if 10%2==0 else "odd"
print(checkeven())
  #(or)
checkeven = lambda n:"even" if n%2==0 else "odd"
print(checkeven(10))
#__________________________________________________________________________________________________________________________________#