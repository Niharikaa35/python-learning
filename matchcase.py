from unittest import case


ch=int(input("enter the number"))
match ch:
    case 1:
        print("case 1 is executed")
      
    case 2:
                print("case 2 is executed")

    case 3:
                        print("case 3 is executed")

                      
    case _:
                                print("default case is executed")


#Traffic is light color is red vechile stop ornage get ready to go green go other color means wrong color

traffic_light=str(input("enter the traffic light color"))

match traffic_light:
        case "red":
                print("vechile stop")

        case "orange":
            print("vechile get ready to go")

        case "green":
            print("vechile go")

        case _:
            print("wrong color")



#match case for sides 
sides=int(input("enter the sides of triangle"))
match sides:
        case 1:
                print("is is not a traiangle")
        case 2:
                        print("is is not a traiangle")
        case 3:
                        print("is is a triangle")

#based on number display the day of the week
day=int(input("enter the number"))
match day:
        case 1:
                print("monday")
        case 2:
                print("tuesday")
        case 3:
                print("wednesday")
        case 4:
                print("thursday")
        case 5:
                print("friday")
        case 6:
                print("saturday")
        case 6:
                print("saturday")
        case _:
                print("invalid day")


#operation of 2 numbers based on operator symbol

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
operator=str(input("enter the operator symbol"))

match operator:
        case "+":
                print(num1+num2)
                
        case "-":
                print(num1-num2)   

        case "*":
                print(num1*num2)
        case "/":
                print(num1/num2)
        case _:
                print("invalid operator")

# enter the 2 numbers and operator symbol to perform the operation if 1 is entered addition will be performed if 2 is entered subtraction will be performed if 3 is entered multiplication will be performed if 4 is entered division will be performed any other number will display invalid operator

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
operator=int(input("enter the operator number"))
match operator:
        case 1:
                print(num1+num2)
                
        case 2:
                print(num1-num2)   

        case 3:
                print(num1*num2)
        case 4:
                print(num1/num2)
        case _:
                print("invalid operator")